"""Define Money Class."""
from typing import Any


class Money:
    """Define Money Class."""

    def __init__(self: "Money", amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency

    # [Fix for Lint] Incompatible overrides
    # https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
    def __eq__(self: "Money", inp: Any) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
        # Check instance's Currency
        if self.currency == inp.currency:
            return self.amount == inp.amount
        return False

    def equals(self: "Money", inp: "Money") -> bool:
        """equal."""
        return self == inp

    def times(self: "Money", multiplier: int) -> "Money":
        """multiplication."""
        return Money(self.amount * multiplier, self.currency)

    def plus(self: "Money", addend: "Money") -> "Sum":
        """plus."""
        return Sum(self, addend)

    def reduce(self: "Money", currency: str) -> "Money":
        """reduce."""
        return self

    def get_currency(self: "Money") -> str:
        """currency."""
        return self.currency

    @staticmethod
    def dollar(amount: int) -> "Money":
        """Instantiate Dollar."""
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        """Instantiate Franc."""
        return Money(amount, "CHF")


class Bank:
    """Define Bank Class."""

    def reduce(self: "Bank", inp: Any, currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return inp.reduce(currency)


class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend

    def reduce(self: "Sum", currency: str) -> "Money":
        """reduce."""
        amount = self.augend.amount + self.addend.amount
        return Money(amount, currency)
