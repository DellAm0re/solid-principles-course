"""ISP: пристрої реалізують тільки потрібні їм інтерфейси."""
from typing import Protocol

class Printer(Protocol):
    def print_document(self, text: str) -> str: ...

class Scanner(Protocol):
    def scan_document(self) -> str: ...

class SimplePrinter:
    def print_document(self, text: str) -> str:
        return f"Надруковано: {text}"

class MultifunctionDevice:
    def print_document(self, text: str) -> str:
        return f"Надруковано: {text}"

    def scan_document(self) -> str:
        return "Відсканований документ"

def print_report(device: Printer, report: str) -> str:
    return device.print_document(report)

def scan_contract(device: Scanner) -> str:
    return device.scan_document()

def demo() -> str:
    basic = SimplePrinter()
    multi = MultifunctionDevice()
    return "\n".join((print_report(basic, "Звіт"), print_report(multi, "Звіт"), scan_contract(multi)))

if __name__ == "__main__":
    print(demo())
