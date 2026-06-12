import pytest
from knowledge_base import KnowledgeBase

def test_faqs_present():
    kb = KnowledgeBase()
    faqs = kb.get_faqs()
    assert isinstance(faqs, list)
    assert len(faqs) >= 3
    assert "What is the pricing model?" in faqs

def test_article_retrieval():
    kb = KnowledgeBase()
    article = kb.get_article("API Integration")
    assert article is not None
    assert "API key" in article
