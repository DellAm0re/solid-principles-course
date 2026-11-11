"""DIP: NotificationService залежить від абстракції MessageSender."""
from typing import Protocol

class MessageSender(Protocol):
    def send(self, recipient: str, text: str) -> str: ...

class EmailSender:
    def send(self, recipient: str, text: str) -> str:
        return f"Email до {recipient}: {text}"

class SmsSender:
    def send(self, recipient: str, text: str) -> str:
        return f"SMS до {recipient}: {text}"

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, recipient: str, text: str) -> str:
        return self.sender.send(recipient, text)

def demo() -> str:
    return "\n".join((
        NotificationService(EmailSender()).notify("student@example.com", "Пара о 10:00"),
        NotificationService(SmsSender()).notify("+380000000000", "Пара о 10:00"),
    ))

if __name__ == "__main__":
    print(demo())
