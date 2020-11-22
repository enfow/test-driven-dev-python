"""Define Dollar Class."""
# for return Dollar itself at method times()
from __future__ import annotations


class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    # [Fix for Lint] Incompatible overrides
    # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
    def __eq__(self, inp: Dollar) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        # If amount attribute is same, it is same instance.
        return self.amount == inp.amount

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.amount * multiplier)

    def equals(self, inp: Dollar) -> bool:
        """equal."""
        return self == inp
