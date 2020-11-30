"""Define Money Class."""
from typing import Any, Tuple


class Money:
    """Define Money Class."""

    def __init__(self: "Money", amount: int, currency: str) -> None:
        """initialize."""
        self.amount = amount
        self.currency = currency

    def __eq__(self: "Money", inp: Any) -> bool:  # type: ignore[override]
        """Define what is equal instance."""
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

    def reduce(self: "Money", bank:"Bank", currency: str) -> "Money":
        """reduce."""
        rate = bank.rate(self.currency, currency)
        return Money(self.amount / rate, currency)

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

    def __init__(self: "Bank") -> None:
        self.rates = dict()

    def reduce(self: "Bank", inp: Any, currency: str) -> "Money":
        """Reduce `money` param to `currency` param."""
        return inp.reduce(self, currency)

    def add_rate(self: "Bank", in_currency: str, out_currency: str, rate: int) -> None:
        """update rate."""
        self.rates[(in_currency, out_currency)] = rate

    def rate(self: "Bank", in_currency: str, out_currency: str) -> int:
        """rate."""
        if in_currency == out_currency:
            return 1
        return self.rates[(in_currency, out_currency)]

class Sum:
    """Define Sum Clsss."""

    def __init__(self: "Sum", augend: "Money", addend: "Money") -> None:
        """Initialize."""
        self.augend = augend
        self.addend = addend

    def reduce(self: "Sum", bank: "Bank", currency: str) -> "Money":
        """reduce."""
        amount = self.augend.amount + self.addend.amount
        return Money(amount, currency)
