# Ch12 드디어, 더하기

- 새로운 기능, Money를 더하는 기능을 추가하려고 한다.
- 더하기는 같은 통화끼리 더하는 것과 다른 통화끼리 더하는 것 두 가지로 나누어 볼 수 있다.

## Trial 1

- 같은 통화의 `Money`끼리 더하는 것부터 테스트하는 `test_simple_addition()`을 먼저 작성하고 이를 통과하는 Code를 작성한다.

#### test

- 5 dollar 두 개를 합하여 10 dollar가 나오는지 확인하는 Test Code를 추가했다.

```python
def test_simple_addition(self):
    summation = Money.dollar(5).plus(Money.dollar(5))
    assert Money.dollar(10) == summation
```

#### code

- `Money` Class에 다음과 같이 `plus()` Method를 새로 작성한 구현하면 Test Code도 통과할 수 있다.

```python
def plus(self: "Money", added: "Money") -> "Money":
    """plus."""
    return Money(self.amount + added.amount, self.currency)
```

#### result

```bash
tests/test_ch12.py::TestMoney::test_currency PASSED
tests/test_ch12.py::TestMoney::test_multiplication PASSED
tests/test_ch12.py::TestMoney::test_equals PASSED
tests/test_ch12.py::TestMoney::test_simple_addition PASSED
```

## Trial 2

- 위에서 구현한 `plus()` Method는 동일한 통화를 가정하고 있다. 다른 통화 간의 더하기가 제대로 이뤄지는지도 함께 체크하기 위해서는 Test Code에 변화가 필요하다.
- 

#### test 1

- 같은 통화를 가정하는 `summation` 대신 dollar를 기준으로 환전한 후를 의미하는 `reduced`가 10 dollar와 같은지 확인하도록 Test Code를 변경한다.

```python
def test_simple_addition(self):
    summation = Money.dollar(5).plus(Money.dollar(5))
    assert Money.dollar(10) == reduced
```

#### test 2

- 서로 다른 통화 간의 연산을 위해서는 어느 한 통화로 맞춰주는 `은행`의 기능이 필요하다.

```python
def test_simple_addition(self):
    summation = Money.dollar(5).plus(Money.dollar(5))
    bank = Bank()
    reduced = bank.reduce(summation, "USD")
    assert Money.dollar(10) == reduced
```

#### result

- Bank() Class가 정의되어 있지 않으므로 Error가 발생했다.

```bash
>       bank = Bank()
E       NameError: name 'Bank' is not defined

tests/test_ch12.py:32: NameError
```

## Trial 3

#### code 

- `Bank` Class를 추가로 구현해주었다.

```python
class Bank:
    """Define Bank Class."""
    pass
```

#### result

- `Bank` Class에 `reduce()` Method를 구현해주어야 할 것 같다.

```bash
        bank = Bank()
>       reduced = bank.reduce(summation, "USD")
E       AttributeError: 'Bank' object has no attribute 'reduce'

tests/test_ch12.py:33: AttributeError
```

## Trial 4

#### code 

- `Bank` Class에 `reduce` Method를 추가해주었다.

```python
class Bank:
    """Define Bank Class."""
    
    def reduce(self: "Bank", money: "Money", currency: str):
        """reduce `money` param to `currency` param."""
        pass
```

#### result

- `reduce()` Method의 반환 값이 없어 값을 비교하는 Test를 통과하지 못한다.

```bash
>       assert Money.dollar(10) == reduced
...
>       if self.currency == inp.currency:
E       AttributeError: 'NoneType' object has no attribute 'currency'

ch12/money.py:18: AttributeError
```

## Trial 5

#### code 

- 일단은 빠르게 Test를 통과하기 위해 `reduce()`의 반환값을 임의로 설정한다.

```python
class Bank:
    """Define Bank Class."""
    
    def reduce(self: "Bank", money: "Money", currency: str):
        """reduce `money` param to `currency` param."""
        return Money(10, "USD")
```

#### result

- 찜찜하지만 모든 Test를 통과했다. 이제 리펙토링을 해주면 된다.

```bash
tests/test_ch12.py::TestMoney::test_multiplication PASSED
tests/test_ch12.py::TestMoney::test_equals PASSED
tests/test_ch12.py::TestMoney::test_simple_addition PASSED
```

