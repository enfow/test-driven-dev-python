# Ch7 사과와 오렌지

- (ch6에서 계속) 5 `Dollar`와 5 `Franc`은 서로 다르므로 이에 대한 Test Code를 작성한다.

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
        # Return False When comparing difference currenct
        assert not Dollar(5).equals(Franc(5))
        assert not Franc(5).equals(Dollar(5))
```

#### code

- 기존 code에는 객체의 `amount` 값만을 가지고 비교하므로 test를 통과하지 못한다.

```python
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
```

#### result

```bash
    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
        # Return False When comparing difference currenct
>       assert not Dollar(5).equals(Franc(5))
E       assert not True
E        +  where True = <bound method Money.equals of <ch6.dollar.Dollar object at 0x104014750>>(<ch6.franc.Franc object at 0x104014710>)
E        +    where <bound method Money.equals of <ch6.dollar.Dollar object at 0x104014750>> = <ch6.dollar.Dollar object at 0x104014750>.equals
E        +      where <ch6.dollar.Dollar object at 0x104014750> = Dollar(5)
E        +    and   <ch6.franc.Franc object at 0x104014710> = Franc(5)
```

## Trial 2

- Test Code를 통과하기 위해 Instance의 Class를 비교하도록 한다.

#### code

```python
class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Any) -> bool:
        """Define what is equal instance."""
        # Check instance's Class Name
        if self.__class__.__name__ == inp.__class__.__name__:
            return self.amount == inp.amount
        return False

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp
```

#### result

```bash
tests/test_ch7.py::TestMoney::test_multiplication PASSED
tests/test_ch7.py::TestMoney::test_equals PASSED
```
