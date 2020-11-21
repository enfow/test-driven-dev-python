# Ch2 타락한 객체

## Trial 1

- (ch1에서 계속) 2 뿐만 아니라 3 또한 곱해주는 경우에 대해서도 Test Code를 추가해준다.
- 기존 Code로는 Test를 통과하지 못한다.

#### test

```python
class TestDollar:
    """Test Dollar"""
    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
        five.times(3)
        assert 15 == five.amount
```

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount 

    def times(self, multiplier: int):
        """multiplication."""
        self.amount = self.amount * multiplier
```

#### result

```bash
    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
        five.times(3)
>       assert 15 == five.amount
E       assert 15 == 30
E         +15
E         -30
```

## Trial 2

- `times()`를 수행할 때마다 새로운 객체를 반환하도록 Test Code를 변경한다.
- `Dollar` Class의 `times()`도 이에 맞춰 변경해준다.
- 이렇게 되면 instance `five`의 `amount` 값이 계속 업데이트 되는 문제를 해결할 수 있다.
- test도 통과한다.

#### test

```python
class TestDollar:
    """Test Dollar"""
    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount
```

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount 

    def times(self, multiplier: int):
        """multiplication."""
        # return new object
        return Dollar(self.amount * multiplier)
```

#### result

```bash
tests/test_ch2.py::TestDollar::test_multiplication PASSED
```
