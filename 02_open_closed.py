"""OCP: нові типи знижок додаються без зміни Checkout."""
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float:
        """Повернути суму з урахуванням знижки."""

class NoDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount

class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        if not 0 <= percent <= 100:
            raise ValueError("Знижка має бути від 0 до 100%")
        self.percent = percent

    def apply(self, amount: float) -> float:
        return amount * (1 - self.percent / 100)

class FixedDiscount(Discount):
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Знижка не може бути від'ємною")
        self.value = value

    def apply(self, amount: float) -> float:
        return max(0.0, amount - self.value)

class Checkout:
    def total(self, amount: float, discount: Discount) -> float:
        if amount < 0:
            raise ValueError("Сума не може бути від'ємною")
        return round(discount.apply(amount), 2)

def demo() -> str:
    checkout = Checkout()
    return f"Без знижки: {checkout.total(200, NoDiscount())}; 10%: {checkout.total(200, PercentageDiscount(10))}; фіксована 30: {checkout.total(200, FixedDiscount(30))}"

if __name__ == "__main__":
    print(demo())
