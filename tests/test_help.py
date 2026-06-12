from help import HelpSystem, FAQ
import pytest
from pathlib import Path
import tempfile

def test_load_faqs():
    with tempfile.TemporaryDirectory() as tmpdir:
        faq_file = Path(tmpdir) / 'faq.md'
        with open(faq_file, 'w') as f:
            f.write('# Title 1\nContent 1\n# Title 2\nContent 2')
        help_system = HelpSystem(str(faq_file))
        assert len(help_system.faqs) == 2
        assert help_system.faqs[0].title == 'Title 1'
        assert help_system.faqs[0].content == 'Content 1'
        assert help_system.faqs[1].title == 'Title 2'
        assert help_system.faqs[1].content == 'Content 2'

def test_search():
    with tempfile.TemporaryDirectory() as tmpdir:
        faq_file = Path(tmpdir) / 'faq.md'
        with open(faq_file, 'w') as f:
            f.write('# Title 1\nContent 1\n# Title 2\nContent 2')
        help_system = HelpSystem(str(faq_file))
        results = help_system.search('Title 1')
        assert len(results) == 1
        assert results[0].title == 'Title 1'
        results = help_system.search('Content 2')
        assert len(results) == 1
        assert results[0].title == 'Title 2'
        results = help_system.search('Non-existent')
        assert len(results) == 0
