"""Define Money Class."""
from __future__ import annotations


class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    # [Fix for Lint] Incompatible overrides
    # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
    def __eq__(self, inp: Money) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        # If amount attribute is same, it is same instance.
        return self.amount == inp.amount

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp
