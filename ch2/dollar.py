"""Define Dollar Class."""


class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int) -> object:
        """multiplication."""
        return Dollar(self.amount * multiplier)
