"""Define Dollar Class."""
# for return Dollar itself at method times()
from __future__ import annotations


class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def equals(self, inp: Dollar) -> bool:
        """equal."""
        return self.amount == inp.amount
