# Принципи SOLID — приклади на Python

Навчальний проєкт з дисципліни **«Архітектура та проєктування програмного забезпечення»**. П'ять самостійних робочих прикладів принципів SOLID. Мова: Python 3.10+; сторонні пакети не потрібні.

## Структура

```text
solid-principles-course/
├── solid/
│   ├── 01_single_responsibility.py
│   ├── 02_open_closed.py
│   ├── 03_liskov_substitution.py
│   ├── 04_interface_segregation.py
│   └── 05_dependency_inversion.py
├── tests/
│   └── test_solid.py
├── README.md
└── FORM_ANSWERS.md
```

## Пояснення принципів

| Принцип | Суть | Приклад |
|---|---|---|
| S — Single Responsibility | Клас має одну визначену відповідальність, тобто одну основну причину для зміни | `OrderCalculator` рахує суму, `ReceiptFormatter` форматує чек |
| O — Open/Closed | Код відкритий для розширення та закритий для модифікації стабільної логіки | `Checkout` працює з інтерфейсом `Discount`; нову знижку додають новим класом |
| L — Liskov Substitution | Підтип зберігає контракт базового типу і може замінити його без порушення очікуваної поведінки | `CardPayment` і `CashPayment` відповідають контракту `PaymentProcessor` |
| I — Interface Segregation | Клієнт не повинен залежати від методів, які не використовує | Окремі протоколи `Printer` та `Scanner` |
| D — Dependency Inversion | Високорівнева логіка залежить від абстракцій, а не конкретних реалізацій | `NotificationService` отримує `MessageSender` ззовні |

## Запуск

Запустіть команди **з кореневої папки проєкту**:

```bash
python solid/01_single_responsibility.py
python solid/02_open_closed.py
python solid/03_liskov_substitution.py
python solid/04_interface_segregation.py
python solid/05_dependency_inversion.py
python -m unittest discover -s tests -v
```
