"""Test codes."""

from ch8.money import Money


class TestMoney:
    """Test Money"""

    def test_multiplication(self):
        five = Money.franc(5)
        assert five.times(2) == Money.franc(10)
        assert five.times(3) == Money.franc(15)
        five = Money.dollar(5)
        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_equals(self):
        assert Money.franc(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.franc(6))
        assert Money.dollar(5).equals(Money.dollar(5))
        assert not Money.dollar(5).equals(Money.dollar(6))
        assert not Money.dollar(5).equals(Money.franc(5))
        assert not Money.franc(5).equals(Money.dollar(5))
