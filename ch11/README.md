# Ch11 모든 악의 근원

- 책에서는 11장에서야 `Dollar`와 `Franc` Class를 지우지만 여기서는 10장에서 이미 지웠다. 
- 기존에는 `Dollar`와 `Franc` Instance가 구분되었지만 이제 `Money` Class 하나만 남았다. 이에 따라 Test Code에서 중복으로 이뤄지는 부분들이 있어 제거하려 한다.
- 이와 같이 Test Code에도 중복이 발생하면 제거해야 한다.

## Trial 1

- dollar와 franc에 대해 개별적으로 수행하여 발생하는 중복을 제거한다.

#### test

- `test_multiplication()`에서 franc에 대해서만 이뤄지는 test code를 제거했다. 
- `test_equals()`에서도 franc에 대해서만 이뤄지는 test code를 제거했다. 

```python
class TestMoney:
    """Test Money"""

    def test_currency(self):
        assert "USD" == Money.dollar(1).get_currency()
        assert "CHF" == Money.franc(1).get_currency()

    def test_multiplication(self):
        five_dollar = Money.dollar(5)
        assert five_dollar.times(2) == Money.dollar(10)
        assert five_dollar.times(3) == Money.dollar(15)
        # Check currency with times() method
        five_franc = Money.franc(5)
        assert five_franc.times(2) == five_franc.times(2)
        assert five_dollar.times(2) == five_dollar.times(2)
        assert not five_franc.times(2) == five_dollar.times(2)

    def test_equals(self):
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.dollar(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.dollar(5))

```

#### result

- Code의 변경 없이 수행하는 Test의 개수를 줄였으므로 당연히 통과한다.

```bash
tests/test_ch11.py::TestMoney::test_currency PASSED
tests/test_ch11.py::TestMoney::test_multiplication PASSED
tests/test_ch11.py::TestMoney::test_equals PASSED
```