# Ch3 모두를 위한 평등

## Trial 1

- (ch2에서 계속) 두 객체가 동일한 값을 가지고 있는지 확인하는 새로운 Test Code를 추가한다.
- **값 객체 패턴**이란 객체의 인스턴스 변수가 생성자를 통해 일단 설정된 후에는 결코 변하지 않는 패턴을 말한다.
- `test_equals()`를 가장 빠르게 통과하기 위해 Dollar 객체의 `equals()`가 `True`를 항상 반환하도록 한다.
- 찝찝하지만 가장 빠르게 Test Code를 통과하는 방법이기도 하다.

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

    # 새로운 test code
    def test_equals(self):
        """test code"""
        assert Dollar(5).equals(Dollar(5))
```

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
        return True
```

#### result

```bash
tests/test_ch3.py::TestDollar::test_equals PASSED
```

## trial 2

- Dollar의 `equals()` method가 `False`를 반환해야만 하는 경우에 대해서도 Test Code를 작성한다.
- 이렇게 하면 `equals()`에서 항상 `True`를 반환하도록 했기 때문에 Test를 통과하지 못한다.

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

    def test_equals(self):
        """test code"""
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

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
        return True
```

#### result 

```bash
    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
>       assert not Dollar(5).equals(Dollar(6))
E       assert not True
E        +  where True = <bound method Dollar.equals of <ch3.dollar.Dollar object at 0x1108c7610>>(<ch3.dollar.Dollar object at 0x1108c7590>)
E        +    where <bound method Dollar.equals of <ch3.dollar.Dollar object at 0x1108c7610>> = <ch3.dollar.Dollar object at 0x1108c7610>.equals
E        +      where <ch3.dollar.Dollar object at 0x1108c7610> = Dollar(5)
E        +    and   <ch3.dollar.Dollar object at 0x1108c7590> = Dollar(6)
```

## trial 3

- 각 Instance의 `amount` attribute의 값이 같은지에 따라 bool 값을 반환하도록 하면 Test Code를 통과할 수 있다.

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

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
```

#### result 

```bash
tests/test_ch3.py::TestDollar::test_equals PASSED
```