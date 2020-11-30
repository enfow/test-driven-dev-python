# Ch13 진짜로 만들기

- ch12에서 `Bank` Class의 `reduce()` Method가 항상 `Money(10, "USD")`를 반환하도록 했다. Test는 통과했지만 리펙토링이 필요하다.
- ch12에서도 언급했듯이 Interface `Expression`은 불필요하다고 느껴 만들지 않았다.

## Trial 1

- 더하기 연산을 수행하는데 계속 이어지는 문제는 두 화폐의 통화가 다른 경우 어떻게 처리할 것인가이다. 이를 다루기 위해 `Sum`이라는 Class를 새로 생성하고자 한다.
- 이를 통해 `Money.plus()` Method에서 항상 반환값은 `self.currency`에 맞추던 부분도 제거하려한다. 

#### test

- `Money.plus()` Method가 `Sum` Class를 반환하는지, 각각의 Attribute는 정확히 저장되는지 확인한다.

```python
def test_plus_return_sum(self):
    five_dollar = Money.dollar(5)
    summation = five_dollar.plus(five_dollar)
    assert isinstance(summation, Sum)
    assert five_dollar == summation.augend
    assert five_dollar == summation.addend
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
        if self.currency == inp.currency:
            return self.amount == inp.amount
        return False

    def equals(self: "Money", inp: "Money") -> bool:
        """equal."""
        return self == inp

    def times(self: "Money", multiplier: int) -> "Money":
        """multiplication."""
        return Money(self.amount * multiplier, self.currency)

    def plus(self: "Money", addend: "Money") -> "Sum":
        """plus."""
        return Sum(self, addend)

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


class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", money: "Money", currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return Money(10, "USD")


class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend
```

#### result

- 일단 모든 Test를 통과한다. 하지만 `Bank.reduce()`에서 여전히 `Money(10, "USD")`만을 항상 반환하도록 하고 있는 부분은 그대로이다.

```bash
tests/test_ch13.py::TestMoney::test_currency PASSED
tests/test_ch13.py::TestMoney::test_multiplication PASSED
tests/test_ch13.py::TestMoney::test_equals PASSED
tests/test_ch13.py::TestMoney::test_simple_addition PASSED
```

## Trial 2

- `Bank.reduce()`에서 입력으로는 `Sum` type을 받고, 출력으로는 `Money`를 반환하도록 하고자 한다.

#### test

```python
def test_reduce_sum(self):
    summation = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(summation, "USD")
    assert (Money.dollar(7) == result)
```

#### code

```python
class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", summation: "Sum", currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        amount = summation.augend.amount + summation.addend.amount
        return Money(amount, currency)
```

#### result

- 모두 통과한다. 

```bash
tests/test_ch13.py::TestMoney::test_currency PASSED
tests/test_ch13.py::TestMoney::test_multiplication PASSED
tests/test_ch13.py::TestMoney::test_equals PASSED
tests/test_ch13.py::TestMoney::test_simple_addition PASSED
```

## Trial 3

- `Bank.reduce()`의 코드가 지저분해 보인다.
    - `Sum` Class 뿐만 아니라 다른 경우에 대해서도 처리를 할 수 있어야 한다.
    - 두 단계의 referencing: `amount = summation.augend.amount + summation.addend.amount`

#### code

- `Bank.reduce()`의 내용을 `Sum.reduce()`로 옮긴다.
- 위에서 언급한 두 가지 코드가 지저분한 이유를 완벽하게 해결하지는 못했다. 하지만 기존에 `Bank.reduce()`에서 하나로 처리되던 기능을 `Sum.reduce()`으로 나누어 처리하도록 했기 때문에 `Bank.reduce()`의 입력이 `Sum` type이 아닌 경우도 다룰 수 있게 되었다.

```python
class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", summation: "Sum", currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return summation.reduce(currency)

class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend

    def reduce(self: "Sum", currency: str) -> "Money":
        """reduce."""
        amount = self.augend.amount + self.addend.amount
        return Money(amount, currency)
```

## Trial 4

- `Bank.reduce()`에서 `Sum` type이 아니라 `Money` type을 받는 경우에 대해서도 정상 동작하도록 하고 싶다.
- `Money` type이 들어오는 경우에는 환율을 적용해 특정 currency로 변경이 가능하도록 해야 할 것이다.

#### test

```python
    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result
```

#### result

- `Money`에는 `reduce()` Method가 없다고 Test에 실패했다.

```bash
E       AttributeError: 'Money' object has no attribute 'reduce'

ch13/money.py:54: AttributeError
```

#### Code

- Test에 통과하기 위해 `Money`에 `reduce()` Method를 추가해주고, `Bank.reduce()`에서 `Money` type이 입력으로 들어오는 경우에는 분기하여 `Money.reduce()`로 처리하도록 해 준다. 

```python
class Money:
    """Define Money Class."""

    def __init__(self: "Money", amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency

    ...

    def reduce(self: "Money", currency: str) -> "Money":
        """reduce."""
        return self
    ...


class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", inp: Any, currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return inp.reduce(currency)
```

#### result

```bash
tests/test_ch13.py::TestMoney::test_currency PASSED
tests/test_ch13.py::TestMoney::test_multiplication PASSED
tests/test_ch13.py::TestMoney::test_equals PASSED
tests/test_ch13.py::TestMoney::test_simple_addition PASSED
```