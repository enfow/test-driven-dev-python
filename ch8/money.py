"""Define Money Class."""
from __future__ import annotations

from typing import Any
from ch8.dollar import Dollar
from ch8.franc import Franc


class Money:
    """Define Money Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.amount = amount

    # [Fix for Lint] Incompatible overrides
    # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
    def __eq__(self, inp: Any) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        # Check instance's Class Name
        if self.__class__.__name__ == inp.__class__.__name__:
            # If amount attribute is same, it is same instance.
            return self.amount == inp.amount
        return False

    def equals(self, inp: Money) -> bool:
        """equal."""
        return self == inp
    
    @staticmethod
    def dollar(amount: int) -> Dollar:
        """Instantiate Dollar."""
        return Dollar(amount)
    
    @staticmethod
    def franc(amount: int) -> Franc:
        """Instantiate Franc."""
        return Franc(amount)
