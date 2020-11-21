"""Define Dollar Class."""

class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount:int):
        """initialize."""
        self.amount = amount 

    def times(self, multiplier: int):
        """multiplication."""
        self.amount = self.amount * multiplier

