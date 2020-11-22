"""Define Dollar Class."""
# for return Dollar itself at method times()
from __future__ import annotations


class Dollar:
    """Define Dollar Class."""

    def __init__(self, amount: int) -> None:
        """initialize."""
        self.__amount = amount

    # [Fix for Lint] Incompatible overrides
    # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
    def __eq__(self, inp: Dollar) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        # If amount attribute is same, it is same instance.
        # pylint disable because access to private attribute of `inp`
        return self.__amount == inp.__amount  # pylint: disable=W0212

    def times(self, multiplier: int) -> Dollar:
        """multiplication."""
        return Dollar(self.__amount * multiplier)

    def equals(self, inp: Dollar) -> bool:
        """equal."""
        return self.__amount == inp.__amount  # pylint: disable=W0212
