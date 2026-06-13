from onboarding import OnboardingProcess, OnboardingStep

def test_onboarding_process():
    onboarding = OnboardingProcess()
    assert not onboarding.is_onboarding_completed()

def test_skip_step():
    onboarding = OnboardingProcess()
    onboarding.skip_step(0)
    assert onboarding.steps[0].completed

def test_complete_step():
    onboarding = OnboardingProcess()
    onboarding.complete_step(0)
    assert onboarding.steps[0].completed

def test_is_onboarding_completed():
    onboarding = OnboardingProcess()
    for i in range(len(onboarding.steps)):
        onboarding.complete_step(i)
    assert onboarding.is_onboarding_completed()

def test_get_next_step():
    onboarding = OnboardingProcess()
    assert onboarding.get_next_step() == 0
    onboarding.complete_step(0)
    assert onboarding.get_next_step() == 1

def test_to_json():
    onboarding = OnboardingProcess()
    json_str = onboarding.to_json()
    assert json_str is not None

def test_from_json():
    onboarding = OnboardingProcess()
    json_str = onboarding.to_json()
    new_onboarding = OnboardingProcess.from_json(json_str)
    assert new_onboarding.steps[0].description == onboarding.steps[0].description
