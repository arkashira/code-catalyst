from ab_testing import ABTesting, Page, Variant

def test_add_page():
    ab_testing = ABTesting()
    page = Page("test_page", [Variant("variant1", 1), Variant("variant2", 1)])
    ab_testing.add_page(page)
    assert ab_testing.get_page("test_page") == page

def test_split_traffic():
    ab_testing = ABTesting()
    page = Page("test_page", [Variant("variant1", 1), Variant("variant2", 1)])
    ab_testing.add_page(page)
    traffic_split = ab_testing.split_traffic("test_page")
    assert traffic_split == {"variant1": 0.5, "variant2": 0.5}

def test_get_results():
    ab_testing = ABTesting()
    page = Page("test_page", [Variant("variant1", 1), Variant("variant2", 1)])
    ab_testing.add_page(page)
    results = ab_testing.get_results("test_page")
    assert results == {"variant1": {"CTR": 0.5, "conversion": 0.2}, "variant2": {"CTR": 0.5, "conversion": 0.2}}

def test_get_page_not_found():
    ab_testing = ABTesting()
    assert ab_testing.get_page("non_existent_page") is None

def test_split_traffic_not_found():
    ab_testing = ABTesting()
    assert ab_testing.split_traffic("non_existent_page") == {}

def test_get_results_not_found():
    ab_testing = ABTesting()
    assert ab_testing.get_results("non_existent_page") == {}
