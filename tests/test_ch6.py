"""Test codes."""

from ch6.dollar import Dollar
from ch6.franc import Franc


class TestMoney:
    """Test Money"""

    def test_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
