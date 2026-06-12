import pytest
from onboarding import OnboardingManager

def test_onboarding_time():
    manager = OnboardingManager()
    duration = manager.complete_onboarding()
    # Ensure onboarding completes in under 5 minutes (300 seconds)
    assert duration < 300, f"Onboarding took too long: {duration}s"
