"""Test codes."""

from ch12.money import Bank, Money


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

    def test_simple_addition(self):
        summation = Money.dollar(5).plus(Money.dollar(5))

        bank = Bank()
        reduced = bank.reduce(summation, "USD")
        assert Money.dollar(10) == reduced
