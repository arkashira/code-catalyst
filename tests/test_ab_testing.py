from ab_testing import ABTesting, Version, Test

def test_create_version():
    ab_testing = ABTesting()
    version = ab_testing.create_version("Version 1", {"param1": "value1"})
    assert version.name == "Version 1"
    assert version.parameters == {"param1": "value1"}

def test_create_test():
    ab_testing = ABTesting()
    version1 = ab_testing.create_version("Version 1", {"param1": "value1"})
    version2 = ab_testing.create_version("Version 2", {"param2": "value2"})
    test = ab_testing.create_test("Test 1", [version1, version2], "Target Audience")
    assert test.name == "Test 1"
    assert test.versions == [version1, version2]
    assert test.target_audience == "Target Audience"

def test_run_test():
    ab_testing = ABTesting()
    version1 = ab_testing.create_version("Version 1", {"param1": "value1"})
    version2 = ab_testing.create_version("Version 2", {"param2": "value2"})
    test = ab_testing.create_test("Test 1", [version1, version2], "Target Audience")
    ab_testing.run_test(test)
    assert test.results == {"Version 1": 50, "Version 2": 50}

def test_view_results():
    ab_testing = ABTesting()
    version1 = ab_testing.create_version("Version 1", {"param1": "value1"})
    version2 = ab_testing.create_version("Version 2", {"param2": "value2"})
    test = ab_testing.create_test("Test 1", [version1, version2], "Target Audience")
    ab_testing.run_test(test)
    results = ab_testing.view_results(test)
    assert results == {"Version 1": 50, "Version 2": 50}

def test_compare_results():
    ab_testing = ABTesting()
    version1 = ab_testing.create_version("Version 1", {"param1": "value1"})
    version2 = ab_testing.create_version("Version 2", {"param2": "value2"})
    test = ab_testing.create_test("Test 1", [version1, version2], "Target Audience")
    test.results = {"Version 1": 60, "Version 2": 40}
    comparison = ab_testing.compare_results(test)
    assert comparison == "Version 1 performs better"
