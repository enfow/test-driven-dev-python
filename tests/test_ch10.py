"""Test codes."""

from ch10.money import Money


class TestMoney:
    """Test Money"""

    def test_currency(self):
        assert "USD" == Money.dollar(1).get_currency()
        assert "CHF" == Money.franc(1).get_currency()

    def test_multiplication(self):
        # Check franc
        five_franc = Money.franc(5)
        assert five_franc.times(2) == Money.franc(10)
        assert five_franc.times(3) == Money.franc(15)
        # Check dollar
        five_dollar = Money.dollar(5)
        assert five_dollar.times(2) == Money.dollar(10)
        assert five_dollar.times(3) == Money.dollar(15)
        # Check currency with times() method
        assert five_franc.times(2) == five_franc.times(2)
        assert five_dollar.times(2) == five_dollar.times(2)
        assert not five_franc.times(2) == five_dollar.times(2)

    def test_equals(self):
        assert Money.franc(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.franc(6))
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.dollar(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.dollar(5))
