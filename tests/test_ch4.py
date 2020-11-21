"""Test codes."""

from ch4.dollar import Dollar


class TestDollar:
    """Test Dollar"""

    def test_multiplication(self):
        """test code"""
        five = Dollar(5)
        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equals(self):
        assert Dollar(5).equals(Dollar(5))
        assert not Dollar(5).equals(Dollar(6))
