"""Define Franc Class."""
# for return Franc itself at method times()
from __future__ import annotations

from ch8.money import Money


class Franc(Money):
    """Define Franc Class."""

    def times(self, multiplier: int) -> Franc:
        """multiplication."""
        return Franc(self.amount * multiplier)
