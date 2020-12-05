"""Test codes."""

from ch15.money import Bank, Money, Sum


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

    def test_plus_return_sum(self):
        five_dollar = Money.dollar(5)
        summation = five_dollar.plus(five_dollar)
        assert isinstance(summation, Sum)
        assert five_dollar == summation.augend
        assert five_dollar == summation.addend

    def test_reduce_sum(self):
        summation = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(summation, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    def test_reduce_money_difference_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_identity_rate(self):
        bank = Bank()
        assert bank.rate("USD", "USD") == 1

    def test_mixed_addition(self):
        five_dollar = Money.dollar(5)
        ten_franc = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(ten_franc.plus(five_dollar), "USD")
        assert Money.dollar(10) == result, "{}".format(result.amount)
