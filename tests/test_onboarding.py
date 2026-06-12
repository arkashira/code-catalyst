from onboarding import OnboardingProcess, Feature

def test_start_onboarding():
    onboarding = OnboardingProcess()
    # Test that the onboarding process covers key features and functionality
    assert len(onboarding.get_features()) == 3

def test_get_features():
    onboarding = OnboardingProcess()
    features = onboarding.get_features()
    assert len(features) == 3
    assert features[0].name == "Dashboard"
    assert features[1].name == "Settings"
    assert features[2].name == "Support"

def test_get_feature_by_name():
    onboarding = OnboardingProcess()
    feature = onboarding.get_feature_by_name("Dashboard")
    assert feature is not None
    assert feature.name == "Dashboard"
    assert feature.description == "Overview of the platform"

def test_get_feature_by_name_not_found():
    onboarding = OnboardingProcess()
    feature = onboarding.get_feature_by_name("Non-existent feature")
    assert feature is None
