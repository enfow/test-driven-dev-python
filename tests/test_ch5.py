"""Test codes."""

from ch5.dollar import Dollar
from ch5.franc import Franc


class TestFranc:
    """Test Franc"""

    def test_multiplication(self):
        five = Franc(5)
        assert five.times(2) == Franc(10)
        assert five.times(3) == Franc(15)

    def test_equals(self):
        assert Franc(5).equals(Franc(5))
        assert not Franc(5).equals(Franc(6))


class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
