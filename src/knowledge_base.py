from typing import List, Dict, Optional

class KnowledgeBase:
    """
    Simple in-memory knowledge base with FAQs and articles.
    """
    _faqs: List[str] = [
        "How do I reset my password?",
        "What is the pricing model?",
        "How do I integrate with the API?",
    ]

    _articles: Dict[str, str] = {
        "Getting Started": "Welcome to Code Catalyst! To get started, create an account...",
        "API Integration": "To integrate with our API, first obtain your API key...",
        "Troubleshooting": "If you encounter errors, check the logs and ensure your environment variables are set...",
    }

    def get_faqs(self) -> List[str]:
        return list(self._faqs)

    def get_article(self, title: str) -> Optional[str]:
        return self._articles.get(title)
