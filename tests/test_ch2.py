"""Test codes."""

from ch2.dollar import Dollar


class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
        product = five.times(3)
        assert 15 == product.amount
