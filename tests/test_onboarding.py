import pytest
import os
from onboarding import Onboarding, Step

@pytest.fixture
def onboarding():
    onboarding = Onboarding([])
    onboarding.add_step("Welcome", "Welcome to ProtoLaunch!")
    onboarding.add_step("Features", "Learn about key features.")
    onboarding.add_step("Workflows", "Understand the workflows.")
    return onboarding

def test_add_step(onboarding):
    assert len(onboarding.steps) == 3
    assert onboarding.steps[0].title == "Welcome"
    assert onboarding.steps[0].description == "Welcome to ProtoLaunch!"

def test_next_step(onboarding):
    step = onboarding.next_step()
    assert step.title == "Welcome"
    assert step.description == "Welcome to ProtoLaunch!"
    assert onboarding.current_step == 1

def test_skip_step(onboarding):
    step = onboarding.skip_step()
    assert step.title == "Welcome"
    assert step.description == "Welcome to ProtoLaunch!"
    assert step.completed
    assert onboarding.current_step == 1

def test_mark_completed(onboarding):
    onboarding.next_step()
    onboarding.mark_completed()
    assert onboarding.steps[0].completed

def test_save_and_load(onboarding, tmp_path):
    filepath = tmp_path / "onboarding.json"
    onboarding.save(filepath)
    loaded_onboarding = Onboarding.load(filepath)
    assert loaded_onboarding.current_step == onboarding.current_step
    assert len(loaded_onboarding.steps) == len(onboarding.steps)
    for i, step in enumerate(loaded_onboarding.steps):
        assert step.title == onboarding.steps[i].title
        assert step.description == onboarding.steps[i].description
        assert step.completed == onboarding.steps[i].completed

def test_to_dict(onboarding):
    data = onboarding.to_dict()
    assert data['current_step'] == 0
    assert len(data['steps']) == 3
    assert data['steps'][0]['title'] == "Welcome"
    assert data['steps'][0]['description'] == "Welcome to ProtoLaunch!"

def test_from_dict():
    data = {
        'steps': [
            {'title': 'Welcome', 'description': 'Welcome to ProtoLaunch!', 'completed': False},
            {'title': 'Features', 'description': 'Learn about key features.', 'completed': False},
            {'title': 'Workflows', 'description': 'Understand the workflows.', 'completed': False}
        ],
        'current_step': 0
    }
    onboarding = Onboarding.from_dict(data)
    assert onboarding.current_step == 0
    assert len(onboarding.steps) == 3
    assert onboarding.steps[0].title == "Welcome"
    assert onboarding.steps[0].description == "Welcome to ProtoLaunch!"
