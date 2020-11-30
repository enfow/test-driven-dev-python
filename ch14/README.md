# Ch14 바꾸기

- 통화가 다른 경우 하나의 화폐로 환율을 적용하여 변경할 수 있도록 하고 싶다.

## Trial 1

#### test

- 통화가 다른 경우에도 `Bank.reduce()`가 제대로 동작하는지, 즉 환율을 적용하여 환전된 결과를 보여주는지 확인하는 Test Code를 작성한다.

```python
def test_reduce_money_difference_currency(self):
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result
```

#### code

- 우선 환율을 알려주는 코드를 작성하려한다. 환전은 은행에서 이뤄지는 것이므로 `Bank` Class 내부에 관련 로직을 생성할 것이다.
- "CHF" -> "USD"의 환율은 일단 2:1로 한다.
- 이에 더해 `Money`의 `reduce()` Method에서 `Bank`로 부터 환율 정보를 불러와 이를 적용하여 반환값을 결정하도록 한다.
- `Sum.reduce()` Method에서는 우선 Interface만 맞춰준다.

```python

class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", inp: Any, currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return inp.reduce(self, currency)

    def rate(self: "Bank", in_currency: str, out_currency: str):
        """rate."""
        if in_currency == "CHF" and out_currency == "USD":
            return 2
        else:
            return 1


class Money:
    """Define Money Class."""

    def __init__(self: "Money", amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency
    
    ...

    def reduce(self: "Money", bank:"Bank", currency: str) -> "Money":
        """reduce."""
        rate = bank.rate(self.currency, currency)
        return Money(self.amount / rate, currency)

    ...


class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend

    def reduce(self: "Sum", bank: "Bank", currency: str) -> "Money":
        """reduce."""
        amount = self.augend.amount + self.addend.amount
        return Money(amount, currency)
```

#### result

- `bank.add_rate()`, 즉 임의의 환율을 적용토록 하는 코드를 아직 작성하지 않아 Test에 실패했지만 다른 부분들은 모두 통과했다.

```bash
tests/test_ch14.py::TestMoney::test_currency PASSED
tests/test_ch14.py::TestMoney::test_multiplication PASSED
tests/test_ch14.py::TestMoney::test_equals PASSED
tests/test_ch14.py::TestMoney::test_plus_return_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_money PASSED
tests/test_ch14.py::TestMoney::test_reduce_money_difference_currency FAILED

    def test_reduce_money_difference_currency(self):
        bank = Bank()
>       bank.add_rate("CHF", "USD", 2)
E       AttributeError: 'Bank' object has no attribute 'add_rate'

tests/test_ch14.py:49: AttributeError
```

## Trial 2

- Trial 1의 Test를 아직 통과하지 못했다. 이를 통과하기 위해서는 `add_rate()` Method를 `Bank` Class에 구현해야 한다.
- 현재 Code는 CHF -> USD 에 대해서만 환율을 구할 수 있고, 그 값 또한 2 : 1로 고정되어 있다. `add_rate()`는 이를 임의로 변경할 수도, 새롭게 추가할 수도 있도록 하는 기능을 제공한다. 따라서 화폐 간의 환율 정보를 저장하고 있는 자료구조가 추가적으로 필요해 보인다.

#### code

- JAVA를 사용하는 책에서는 HashTable() 객체를 사용하지만 PYTHON에서는 `dict()`를 사용할 것이다.
- 또한 책에서는 `Pair`라는 새로운 Class를 정의히자만, 여기서는 `Tuple`로 dict()의 Key를 표현할 것이다.

```python
class Bank:
    """Define Bank Class."""

    def __init__(self: "Bank") -> None:
        self.rates = dict()

    def reduce(self: "Bank", inp: Any, currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return inp.reduce(self, currency)

    def add_rate(self: "Bank", in_currency: str, out_currency: str, rate: int) -> None:
        """update rate."""
        self.rates[(in_currency, out_currency)] = rate

    def rate(self: "Bank", in_currency: str, out_currency: str) -> int:
        """rate."""
        return self.rates[(in_currency, out_currency)]
```

#### result

- `add_rate()` 를 구현했지만 이제 다른 곳에서 Test에 실패했다.
- 동일한 화폐인 경우에는 1로 미리 설정해두어야 할 것 같다.

```bash
tests/test_ch14.py::TestMoney::test_currency PASSED
tests/test_ch14.py::TestMoney::test_multiplication PASSED
tests/test_ch14.py::TestMoney::test_equals PASSED
tests/test_ch14.py::TestMoney::test_plus_return_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_money FAILED
tests/test_ch14.py::TestMoney::test_reduce_money_difference_currency PASSED

>       return self.rates[(in_currency, out_currency)]
E       KeyError: ('USD', 'USD')

ch14/money.py:67: KeyError
==============================
```

## Trial 3

- 동일한 화폐 단위에 대해 `reduce()`를 수행하게 되는 경우 rate는 항상 1로 반환토록 한다.

#### test

- 우선 동일 화폐에 대해 `reduce()` 하는 경우에 대한 test code를 추가한다.

```python
def test_identity_rate(self):
    bank = Bank()
    assert bank.rate("USD", "USD") == 1
```

#### code

- `Bank.rate()` Method를 업데이트하여 해결하고자 한다.

```python
class Bank:
    """Define Bank Class."""

    def __init__(self: "Bank") -> None:
        self.rates = dict()

    ...

    def rate(self: "Bank", in_currency: str, out_currency: str) -> int:
        """rate."""
        if in_currency == out_currency:
            return 1
        return self.rates[(in_currency, out_currency)]
```

#### result

- Test를 모두 통과한다.

```bash
tests/test_ch14.py::TestMoney::test_currency PASSED
tests/test_ch14.py::TestMoney::test_multiplication PASSED
tests/test_ch14.py::TestMoney::test_equals PASSED
tests/test_ch14.py::TestMoney::test_plus_return_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_sum PASSED
tests/test_ch14.py::TestMoney::test_reduce_money PASSED
tests/test_ch14.py::TestMoney::test_reduce_money_difference_currency PASSED
tests/test_ch14.py::TestMoney::test_identity_rate PASSED
```