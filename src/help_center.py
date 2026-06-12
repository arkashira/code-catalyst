import json
from dataclasses import dataclass
from typing import List

@dataclass
class Article:
    title: str
    content: str

@dataclass
class SupportTicket:
    id: int
    question: str
    response: str = ""

class HelpCenter:
    def __init__(self):
        self.articles = []
        self.tickets = []

    def add_article(self, title: str, content: str):
        self.articles.append(Article(title, content))

    def submit_support_ticket(self, question: str):
        ticket = SupportTicket(len(self.tickets) + 1, question)
        self.tickets.append(ticket)
        return ticket.id

    def respond_to_ticket(self, ticket_id: int, response: str):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                ticket.response = response
                break

    def get_articles(self):
        return self.articles

    def get_ticket(self, ticket_id: int):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None
