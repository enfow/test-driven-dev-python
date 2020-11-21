"""Test codes."""

from ch1.dollar import Dollar


class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount
