from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class SupportTicket:
    name: str
    email: str
    message: str
    timestamp: datetime

class SupportContact:
    """
    Handles support ticket creation.
    """
    def __init__(self):
        self._tickets: Dict[int, SupportTicket] = {}
        self._next_id: int = 1

    def send_message(self, name: str, email: str, message: str) -> int:
        """
        Create a support ticket and return its ID.
        """
        ticket = SupportTicket(
            name=name,
            email=email,
            message=message,
            timestamp=datetime.utcnow()
        )
        ticket_id = self._next_id
        self._tickets[ticket_id] = ticket
        self._next_id += 1
        return ticket_id

    def get_ticket(self, ticket_id: int) -> SupportTicket:
        return self._tickets[ticket_id]
