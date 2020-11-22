# Ch6 돌아온 '모두를 위한 평등'

- (ch5에서 계속) `Dollar` Class와 `Franc` Class가 중복되는 문제가 있다.
- 중복을 제거하기 위해 `Money`라는 Parent Class를 정의하고 이를 상속하도록 한다.
- code에서 중복을 제거하기에 앞서 Test Code부터 중복을 제거한다.

## Trial 1

#### test

```python
class TestMoney:
    """Test Money"""

    def test_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

#### result

- 사실상 Code, Test Code 모두 바뀐 것이 없기 때문에 Test를 당연히 통과한다.

```bash
tests/test_ch6.py::TestMoney::test_multiplication PASSED
tests/test_ch6.py::TestMoney::test_equals PASSED
```

## Trial 2

- `Money` Class를 정의하고 `Dollar`, `Franc` Class가 이를 상속하도록 한다.

## code

```python
# money.py
class Money:
    """Define Money Class."""

    def __init__(self) -> None:
        """initialize."""
        pass

# dollar.py
class Dollar(Money):
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        super().__init__()
        self.amount = amount

    def __eq__(self, inp: Dollar) -> bool:
        """Define what is equal instance."""
        return self.amount == inp.amount

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def equals(self, inp: Dollar) -> bool:
        """equal."""
        return self == inp

# franc.py
class Franc(Money):
    """Define Franc Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        super().__init__()
        self.amount = amount

    def __eq__(self, inp: Franc) -> bool:
        """Define what is equal instance."""
        return self.amount == inp.amount

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)

    def equals(self, inp: Franc) -> bool:
        """equal."""
        return self == inp
```

#### result

- 새로운 Class를 정의하고 상속하지만 사실상 달라진 것이 없으므로 test 또한 동일하게 통과한다.

```bash
tests/test_ch6.py::TestMoney::test_multiplication PASSED
tests/test_ch6.py::TestMoney::test_equals PASSED
```

## Trail 3

- `Dollar`와 `Franc`에서 중복되는 부분을 `Money`로 옮겨 중복을 제거한다.
- `amount` attribute와 `equals()` method를 `Money`로 옮긴다.

#### code

- Python에서는 Child Class에 `__init__()` method가 정의되어 있지 않으면 Parent Class의 `__init__()`을 사용하므로 Child Class에서 `__init___()`도 제거한다.
  - pylint: Useless super delegation in method '__init__' (useless-super-delegation)

```python
# money.py
class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Money) -> bool:
        """Define what is equal instance."""
        return self.amount == inp.amount

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp

# dollar.py
class Dollar(Money):
    """Define Dollar Class."""

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

# franc.py
class Franc(Money):
    """Define Franc Class."""

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)
```

#### result

- 중복을 제거했지만 여전히 잘 동작하는 코드를 작성했음을 확인할 수 있다.

```bash
tests/test_ch6.py::TestMoney::test_multiplication PASSED
tests/test_ch6.py::TestMoney::test_equals PASSED
```