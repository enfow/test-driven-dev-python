"""Define Dollar Class."""
# for return Dollar itself at method times()
from __future__ import annotations

from ch8.money import Money


class Dollar(Money):
    """Define Dollar Class."""

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)
