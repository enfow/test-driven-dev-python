# Ch15 서로 다른 통화 더하기

- 서로 다른 통화 간에도 환율을 적용하여 더하기 연산을 수행하도록 하고 싶다.

## Trial 1

- 우선 서로 다른 통화를 더하는 Test Code를 작성한다.

#### test

```python
def test_mixed_addition(self):
    five_dollar = Money.dollar(5)
    ten_franc = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(ten_franc.plus(five_dollar), "USD")
    assert Money.dollar(10) == result
```

#### result

- 계산된 결과가 서로 같지 않다고 error가 발생한다.

```python
>       assert Money.dollar(10) == result
E       assert <ch15.money.M...t 0x107af8c50> == <ch15.money.M...t 0x107af8f10>
E         +<ch15.money.Money object at 0x107af8c50>
E         -<ch15.money.Money object at 0x107af8f10>

tests/test_ch15.py:63: AssertionError
```

## Trial 2

#### code

- 기존의 `Sum` Class의 `reduce` Method는 환전을 제대로 고려하지 않고 있다. 따라서 다음과 같이 코드를 변경해준다.

```python
class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend

    def reduce(self: "Sum", bank: "Bank", currency: str) -> "Money":
        """reduce."""
        amount = bank.reduce(self.augend, currency).amount + (bank.reduce(self.addend, currency)).amount
        return Money(amount, currency)
```

#### result

- 모두 통과한다.

```bash
tests/test_ch15.py::TestMoney::test_currency PASSED
tests/test_ch15.py::TestMoney::test_multiplication PASSED
tests/test_ch15.py::TestMoney::test_equals PASSED
tests/test_ch15.py::TestMoney::test_plus_return_sum PASSED
tests/test_ch15.py::TestMoney::test_reduce_sum PASSED
tests/test_ch15.py::TestMoney::test_reduce_money PASSED
tests/test_ch15.py::TestMoney::test_reduce_money_difference_currency PASSED
tests/test_ch15.py::TestMoney::test_identity_rate PASSED
tests/test_ch15.py::TestMoney::test_mixed_addition PASSED
```
