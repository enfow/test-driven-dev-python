# Ch3

## Trial1

- (ch3에서 계속) test code를 개선하면 attribute `amount`를 private로 바꾸어 보다 안전하게(Python?) 할 수 있다.
- TODO List를 확인하며 그에 맞게 test code를 개선하고, 그것을 통과하도록 code를 개선하는 과정의 반복이다.

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int) -> object:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def equals(self, inp: object) -> bool:
        """equal."""
        return self.amount == inp.amount
```

#### test(old)

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

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

#### test(new)

```python
class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

- 그런데 Python에서는 `five.times(2) == Dollar(10)`와 같이 두 instance를 비교하면 항상 `False`를 반환한다.

#### result

```bash
    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
>       assert five.times(2) == Dollar(10)
E       assert <ch4.dollar.D...t 0x104240490> == <ch4.dollar.D...t 0x104240190>
E         +<ch4.dollar.Dollar object at 0x104240490>
E         -<ch4.dollar.Dollar object at 0x104240190>
```

## trial2

- `five.times(2) == Dollar(10)`와 같은 test code를 통과하기 위해서는 code에 `__eq__()` method를 작성해주어야 한다.

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, other):
        if (isinstance(other, Dollar)):
            # If amount attribute is same, it is same instance.
            return self.amount == other.amount
        return False

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def equals(self, inp: Dollar) -> bool:
        """equal."""
        return self.amount == inp.amount
```

#### test

```python
class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

#### result

```bash
tests/test_ch4.py::TestDollar::test_multiplication PASSED
tests/test_ch4.py::TestDollar::test_equals PASSED
```