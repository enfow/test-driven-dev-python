# Ch1

## Trial 1

- 클래스 정의

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int):
        pass

```

#### result

```bash
[Trial 1]

    def test_multiplication(self):
            five = Dollar(5)
            five.times(2)
>       assert 10 == five.amount
E       assert 10 == 5
E         +10
E         -5
```

## Trial 2

- `assert` 간단하게 통과하기

#### code 

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int):
        pass
```

#### result

```bash
tests/test_ch1.py::TestDollar::test_multiplication PASSED
```

## Trial 3

- 중복 제거

#### code 

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount 

    def times(self, multiplier: int):
        self.amount = self.amount * multiplier
```

#### result

```bash
tests/test_ch1.py::TestDollar::test_multiplication PASSED
```
