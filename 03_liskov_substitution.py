"""LSP: будь-який PaymentProcessor підтримує контракт pay(amount)."""
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Для amount > 0 повертає підтвердження успішного платежу."""

class CardPayment(PaymentProcessor):
    def pay(self, amount: float) -> str:
        validate_amount(amount)
        return f"Оплачено карткою: {amount:.2f} грн"

class CashPayment(PaymentProcessor):
    def pay(self, amount: float) -> str:
        validate_amount(amount)
        return f"Оплачено готівкою: {amount:.2f} грн"

def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Сума платежу має бути додатною")

def complete_purchase(processor: PaymentProcessor, amount: float) -> str:
    """Не залежить від конкретного способу оплати."""
    return processor.pay(amount)

def demo() -> str:
    return "\n".join(complete_purchase(p, 150) for p in (CardPayment(), CashPayment()))

if __name__ == "__main__":
    print(demo())
