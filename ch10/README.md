# Ch10 흥미로운 시간

- `Dollar`와 `Franc` Class를 없앤다.
- 이를 위해 `times()` Method를 `Money` Class 내부로 가져오려 한다.

## Trial 1

- `Dollar`와 `Franc`를 제거하고, `Money` Class로 통일한다.
- 이를 위해 `times()` Method를 `Money` Class에 구현한다. 이때 반환 값을 `Money` Class가 된다.

#### test

- `Money` Class의 `times()`에서 Dollar인 경우와 Franc인 경우 모두를 반환하므로 이에 대한 Test Code를 작성한다.

```python
class TestMoney:
    """Test Money"""

    def test_currency(self):
        assert "USD" == Money.dollar(1).get_currency()
        assert "CHF" == Money.franc(1).get_currency()

    def test_multiplication(self):
        # Check franc
        five_franc = Money.franc(5)
        assert five_franc.times(2) == Money.franc(10)
        assert five_franc.times(3) == Money.franc(15)
        # Check dollar
        five_dollar = Money.dollar(5)
        assert five_dollar.times(2) == Money.dollar(10)
        assert five_dollar.times(3) == Money.dollar(15)
        # Check currency with times() method
        assert five_franc.times(2) == five_franc.times(2)
        assert five_dollar.times(2) == five_dollar.times(2)
        assert not five_franc.times(2) == five_dollar.times(2)

    def test_equals(self):
        assert Money.franc(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.franc(6))
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.dollar(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.dollar(5))
```

#### code

```python
class Money:
    """Define Money Class."""

    def __init__(self: "Money", amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency

    def __eq__(self: "Money", inp: Any) -> bool: 
        """Define what is equal instance."""
        if self.__class__.__name__ == inp.__class__.__name__:
            return self.amount == inp.amount
        return False

    def equals(self: "Money", inp: "Money") -> bool:
        """equal."""
        return self == inp

    def times(self: "Money", multiplier: int) -> "Money":
        """multiplication."""
        return Money(self.amount * multiplier, self.currency)

    def get_currency(self: "Money") -> str:
        """currency."""
        return self.currency

    @staticmethod
    def dollar(amount: int) -> "Money":
        """Instantiate Dollar."""
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        """Instantiate Franc."""
        return Money(amount, "CHF")
```

#### result

- 두 곳에서 Test를 통과하지 못했는데 모두 Instance의 타입이 일치하는지 확인하는 부분에서 발생했다.
- 현재 코드에서는 `Dollar`와 `Franc`을 구분하지 못한다.
- `__eq__()` 부분에서 잡아낼 수 있도록 해야한다.

```bash
tests/test_ch10.py::TestMoney::test_multiplication FAILED
tests/test_ch10.py::TestMoney::test_equals FAILED

...

>       assert not five_franc.times(2) == five_dollar.times(2)
E       assert not <ch10.money.M...t 0x111de4250> == <ch10.money.M...t 0x111de4210>
E         +<ch10.money.Money object at 0x111de4250>
E         -<ch10.money.Money object at 0x111de4210>

...

>       assert not Money.dollar(5).equals(Money.franc(5))
E       assert not True
E        +  where True = <bound method Money.equals of <ch10.money.Money object at 0x111dd8290>>(<ch10.money.Money object at 0x111dd83d0>)
E        +    where <bound method Money.equals of <ch10.money.Money object at 0x111dd8290>> = <ch10.money.Money object at 0x111dd8290>.equals
E        +      where <ch10.money.Money object at 0x111dd8290> = <function Money.dollar at 0x111dcc4d0>(5)
E        +        where <function Money.dollar at 0x111dcc4d0> = Money.dollar
E        +    and   <ch10.money.Money object at 0x111dd83d0> = <function Money.franc at 0x111dcc560>(5)
E        +      where <function Money.franc at 0x111dcc560> = Money.franc
```

## Trial 2

- `Money`의 `__eq__()` Method에서 `currency` Attribute를 검사하도록 한다.

#### code

```python
def __eq__(self: "Money", inp: Any) -> bool:
    """Define what is equal instance."""
    # Check instance's Currency, Not Class anymore
    if self.currency == inp.currency:
        return self.amount == inp.amount
    return False
```

#### result

- 모든 Test를 통과한다.

```bash
tests/test_ch10.py::TestMoney::test_currency PASSED
tests/test_ch10.py::TestMoney::test_multiplication PASSED
tests/test_ch10.py::TestMoney::test_equals PASSED
```