# Ch9 우리가 사는 시간

- `Money`의 두 개의 Child Class `Dollar`, `Franc`를 없애기 위해서 `Money`에 Currency 개념을 추가하려 한다.

## Trial 1

- Currency 개념을 추가하기 위해 Child Class에 `get_currency()` Method를 추가하려 한다.
- Test Code 부터 작성한다.

#### test

```python
class TestMoney:
    """Test Money"""

    def test_currency(self):
        assert "USD" == Money.dollar(1).get_currency()
        assert "CHF" == Money.franc(1).get_currency()
        
    def test_multiplication(self):
        five = Money.franc(5)
        assert five.times(2) == Money.franc(10)
        assert five.times(3) == Money.franc(15)
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_equals(self):
        assert Money.franc(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.franc(6))
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.dollar(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.dollar(5))
```

#### code

- `Dollar`, `Franc` Class에 각각 통화단위를 string으로 반환하는 `.get_currency()` Method를 추가했다.

```python
# money.py
class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Any) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        if self.__class__.__name__ == inp.__class__.__name__:
            return self.amount == inp.amount
        return False

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp

    @staticmethod
    def dollar(amount: int) -> Dollar:
        """Instantiate Dollar."""
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        """Instantiate Franc."""
        return Franc(amount)


class Dollar(Money):
    """Define Dollar Class."""

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def get_currency(self) -> str:
        """currency."""
        return "USD"


class Franc(Money):
    """Define Franc Class."""

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)

    def get_currency(self) -> str:
        """currency."""
        return "CHF"
```

#### result

```bash
tests/test_ch9.py::TestMoney::test_currency PASSED
tests/test_ch9.py::TestMoney::test_multiplication PASSED
tests/test_ch9.py::TestMoney::test_equals PASSED
```

## Trial 2

- 중복을 제거하기 위해 `currency` Attribute를 추가하고 이를 `get_currency()` Method에서 반환하는 형태로 바꾸려 한다.

#### code

- `Dollar`와 같이 `Franc` 에 대해서도 동일하게 해 준다.

```python
class Dollar(Money):
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
        self.currency = "USD"  # For `Franc` Class,  self.currency = "CHF"

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def get_currency(self) -> str:
        """currency."""
        return self.currency
```

#### result

```bash
tests/test_ch9.py::TestMoney::test_currency PASSED
tests/test_ch9.py::TestMoney::test_multiplication PASSED
tests/test_ch9.py::TestMoney::test_equals PASSED
```

## Trial 3

- `Dollar`와 `Franc` 모두 동일하게 `currency` Attribute와 `get_currency()` Method를 가지고 있으므로 `Money` Class로 올려버려려 한다.

#### code

```python
class Money:
    """Define Money Class."""

    def __init__(self, amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency

    def __eq__(self, inp: Any) -> bool:
        """Define what is equal instance."""
        if self.__class__.__name__ == inp.__class__.__name__:
            return self.amount == inp.amount
        return False

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp

    def get_currency(self) -> str:
        """currency."""
        return self.currency

    @staticmethod
    def dollar(amount: int) -> Dollar:
        """Instantiate Dollar."""
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Franc:
        """Instantiate Franc."""
        return Franc(amount)


class Dollar(Money):
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        super().__init__(amount, "USD")

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)


class Franc(Money):
    """Define Franc Class."""

    def __init__(self, amount: int) -> None:
        super().__init__(amount, "CHF")

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)
```

#### result

```bash
tests/test_ch9.py::TestMoney::test_currency PASSED
tests/test_ch9.py::TestMoney::test_multiplication PASSED
tests/test_ch9.py::TestMoney::test_equals PASSED
```
