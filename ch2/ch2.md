# Ch2

## Trial 1

- (ch1에서 계속) 새로운 Test code 작성

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

- `times()`를 수행할 때마다 새로운 객체를 반환하도록 Test Code를 변경
- `Dollar` Class의 `times()`도 이에 맞춰 변경

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

#### result

```bash
tests/test_ch2.py::TestDollar::test_multiplication PASSED
```
