from help_center import HelpCenter, Article, SupportTicket

def test_add_article():
    help_center = HelpCenter()
    help_center.add_article("Test Article", "This is a test article.")
    assert len(help_center.get_articles()) == 1
    assert help_center.get_articles()[0].title == "Test Article"
    assert help_center.get_articles()[0].content == "This is a test article."

def test_submit_support_ticket():
    help_center = HelpCenter()
    ticket_id = help_center.submit_support_ticket("This is a test question.")
    assert ticket_id == 1
    assert len(help_center.tickets) == 1
    assert help_center.tickets[0].id == 1
    assert help_center.tickets[0].question == "This is a test question."

def test_respond_to_ticket():
    help_center = HelpCenter()
    ticket_id = help_center.submit_support_ticket("This is a test question.")
    help_center.respond_to_ticket(ticket_id, "This is a test response.")
    assert help_center.get_ticket(ticket_id).response == "This is a test response."

def test_get_articles():
    help_center = HelpCenter()
    help_center.add_article("Test Article 1", "This is a test article 1.")
    help_center.add_article("Test Article 2", "This is a test article 2.")
    articles = help_center.get_articles()
    assert len(articles) == 2
    assert articles[0].title == "Test Article 1"
    assert articles[1].title == "Test Article 2"

def test_get_ticket():
    help_center = HelpCenter()
    ticket_id = help_center.submit_support_ticket("This is a test question.")
    ticket = help_center.get_ticket(ticket_id)
    assert ticket.id == ticket_id
    assert ticket.question == "This is a test question."
