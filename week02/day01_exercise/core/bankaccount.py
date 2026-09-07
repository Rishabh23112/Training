"""Bank account with Encapsulation."""


class BankAccount:
    """Bank accounrt with balance, withdraw, deposit methods."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        """Get current balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposit money. Amount must be positive."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            return False

        self._balance -= amount
        return True

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return f"BankAccount(owner={self.owner!r}, " f"balance={self._balance!r})"
