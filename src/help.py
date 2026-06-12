import json
import re
from dataclasses import dataclass
from pathlib import Path

@dataclass
class FAQ:
    title: str
    content: str

class HelpSystem:
    def __init__(self, faq_file: str):
        self.faq_file = faq_file
        self.faqs = self.load_faqs()

    def load_faqs(self):
        faqs = []
        with open(self.faq_file, 'r') as f:
            lines = f.readlines()
            title = None
            content = []
            for line in lines:
                if line.startswith('# '):
                    if title:
                        faqs.append(FAQ(title, '\n'.join(content)))
                    title = line.strip()[2:]
                    content = []
                else:
                    content.append(line.strip())
            if title:
                faqs.append(FAQ(title, '\n'.join(content)))
        return faqs

    def search(self, query: str):
        results = []
        for faq in self.faqs:
            if re.search(query, faq.title + faq.content, re.IGNORECASE):
                results.append(faq)
        return results
