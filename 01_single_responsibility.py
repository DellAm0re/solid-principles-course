"""SRP: обчислення суми замовлення відокремлено від формування чека."""
from dataclasses import dataclass

@dataclass(frozen=True)
class OrderItem:
    name: str
    price: float
    quantity: int

class OrderCalculator:
    """Відповідає тільки за обчислення вартості."""
    def total(self, items: list[OrderItem]) -> float:
        if any(item.price < 0 or item.quantity < 0 for item in items):
            raise ValueError("Ціна та кількість мають бути невід'ємними")
        return round(sum(item.price * item.quantity for item in items), 2)

class ReceiptFormatter:
    """Відповідає тільки за текстове представлення чека."""
    def format(self, items: list[OrderItem], total: float) -> str:
        lines = [f"{item.name}: {item.quantity} × {item.price:.2f} грн" for item in items]
        return "\n".join([*lines, f"Разом: {total:.2f} грн"])

def demo() -> str:
    items = [OrderItem("Зошит", 25.0, 2), OrderItem("Ручка", 15.0, 1)]
    return ReceiptFormatter().format(items, OrderCalculator().total(items))

if __name__ == "__main__":
    print(demo())
