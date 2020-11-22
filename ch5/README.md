# Ch5 솔직히 말하자면

- Class `Dollar`에 이어 다른 화폐인 `Franc`에 대해서도 Class를 작성하고자 한다.
- 단위만 다를 뿐 동일한 화폐이므로 `Franc`에 대해서도 `Dollar`와 동일한 Test code를 작성한다.
- 이때 동일한 Test code를 통과하는 가장 빠른 방법은 `Dollar` Class의 정의를 복사하여 `Franc` Class의 정의에 그대로 붙여 넣는 것이다.

## Trial 1

#### test

- `Dollar`에 적용된 test code에서 class 이름만 바꾸어 `Franc`의 test code를 작성한다.

```python
class TestFranc:
    """Test Franc"""

    def test_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)

    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))


class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

#### code

- code 또한 `Dollar` class에서 이름만 변경한 것으로 한다.

```python
class Franc:
    """Define Franc Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def __eq__(self, inp: Franc) -> bool:
        """Define what is equal instance."""
        return self.amount == inp.amount

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)

    def equals(self, inp: Franc) -> bool:
        """equal."""
        return self.amount == inp.amount
```

#### result

```bash
tests/test_ch5.py::TestFranc::test_multiplication PASSED
tests/test_ch5.py::TestFranc::test_equals PASSED
tests/test_ch5.py::TestDollar::test_multiplication PASSED
tests/test_ch5.py::TestDollar::test_equals PASSED
```
