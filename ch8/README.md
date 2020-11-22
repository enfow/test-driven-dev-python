# Ch8 객체 만들기

- (ch7에서 계속) `Money` Class로 구현을 많이 이동하다보니 `Dollar`와 `Franc`에서 하는 일이 많이 없어졌다. `times()` Method도 `Money` Class로 옮겨 중복을 한 번 더 제거할 수 있을 것이다.
- 이렇게 되면 Child Class를 제거할 수도 있어 보인다.
- Child Class를 제거하기 위한 전초작업으로 `Money` Class에서 `Dollar`, `Franc` 객체를 생성하도록 하는 작업을 진행하려한다.

## Trial 1

- `Money` Class에서 `Dollar` 객체를 생성할 수 있도록 Test Code를 작성한다.

#### test

```python
class TestMoney:
    """Test Money"""

    def test_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        # Return False When comparing difference currenct
        assert not Money.dollar(5).equals(Franc(5))
        assert not Franc(5).equals(Money.dollar(5))
```

#### result

- 아직 `Money` Class에는 `dollar()` Method가 없으므로 Test를 통과할 수 없다.

```bash
E       AttributeError: type object 'Money' has no attribute 'dollar'
```

## Trial 2

- Test를 통과하기 위해 `Money` Class에 Static Method `dollar()`를 추가하여 `Dollar` Instance를 생성하도록 한다.
- 이렇게 Instance를 생성하는 Method를 Factory Method라고 한다.

#### code

```python
class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Any) -> bool: 
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
```

#### result

```bash
tests/test_ch8.py::TestMoney::test_multiplication PASSED
tests/test_ch8.py::TestMoney::test_equals PASSED
```

## Trial 3

- `Franc()` Class에 대해서도 동일한 Test Code를 작성해주고, 그에 맞춰 Code를 개선한다.

#### test

```python
class TestMoney:
    """Test Money"""

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

```python
class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Any) -> bool: 
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
```

#### result

```bash
tests/test_ch8.py::TestMoney::test_multiplication PASSED
tests/test_ch8.py::TestMoney::test_equals PASSED
```