import pytest
from support import SupportContact

def test_support_ticket_creation():
    support = SupportContact()
    ticket_id = support.send_message(
        name="Alice",
        email="alice@example.com",
        message="Need help with API integration."
    )
    assert isinstance(ticket_id, int)
    ticket = support.get_ticket(ticket_id)
    assert ticket.name == "Alice"
    assert ticket.email == "alice@example.com"
    assert ticket.message == "Need help with API integration."
