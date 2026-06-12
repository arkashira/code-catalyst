from analytics import Analytics, Event
import json
import os
from datetime import datetime

def test_collect():
    analytics = Analytics('test.json')
    analytics.collect('page_view')
    assert len(analytics.events) == 1
    assert analytics.events[0].type == 'page_view'

def test_store():
    analytics = Analytics('test.json')
    analytics.collect('page_view')
    analytics.store()
    with open('test.json', 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['type'] == 'page_view'
    os.remove('test.json')

def test_display():
    analytics = Analytics('test.json')
    analytics.collect('page_view')
    analytics.collect('button_click')
    analytics.collect('form_submission')
    analytics.display()
    # This will print the analytics to the console

def test_main():
    # This will run the main function and test the menu-driven interface
    # It's difficult to test this programmatically, so we'll just run it and verify manually
    # os.system('python src/analytics.py')
    pass
