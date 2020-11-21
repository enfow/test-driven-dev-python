# Ch1 다중 통화를 지원하는 Money 객체

## Trial 1

- 가장 처음으로 통과해야 할 것은 test에서 요구하는 Interface를 갖춘 class를 정의하는 것이다.

### test

```python
class TestDollar:
    """Test Dollar"""
    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
```

#### code

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int) -> None:
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int) -> None:
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

- Interface를 정의하였다면 첫 번째 `assert` 문인 `assert 10 == five.amount`를 통과하도록 한다.

#### code 

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int) -> None:
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int) -> None:
        self.amount = 5 * 2
```

#### result

```bash
tests/test_ch1.py::TestDollar::test_multiplication PASSED
```

## Trial 3

- 위의 예시에서 `times()` method에서 사용되는 `5 * 2` 중 5는 amount attribute, 2는 multiplier parameter 값이기도 하다.
- 중복을 줄여주는 차원에서 다음과 같이 대체가 가능하다.
- test도 마찬가지로 통과한다.

#### code 

```python
class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int) -> None:
        """initialize."""
        self.amount = amount 

    def times(self, multiplier: int) -> None:
        self.amount = self.amount * multiplier
```

#### result

```bash
tests/test_ch1.py::TestDollar::test_multiplication PASSED
```
