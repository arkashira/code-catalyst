from ab_testing import ABTesting, Page, Variant

def test_add_page():
    ab_testing = ABTesting()
    page = Page("example", [Variant("A", 1), Variant("B", 1), Variant("C", 1)])
    ab_testing.add_page(page)
    assert page.name in ab_testing.pages

def test_split_traffic():
    ab_testing = ABTesting()
    page = Page("example", [Variant("A", 1), Variant("B", 1), Variant("C", 1)])
    ab_testing.add_page(page)
    traffic_split = ab_testing.split_traffic("example")
    assert traffic_split == {"A": 1/3, "B": 1/3, "C": 1/3}

def test_display_results():
    ab_testing = ABTesting()
    page = Page("example", [Variant("A", 1), Variant("B", 1), Variant("C", 1)])
    ab_testing.add_page(page)
    results = {
        "A": {"CTR": 10, "conversion": 5},
        "B": {"CTR": 15, "conversion": 10},
        "C": {"CTR": 8, "conversion": 3}
    }
    ab_testing.display_results("example", results)

def test_traffic_split_custom_ratio():
    ab_testing = ABTesting()
    page = Page("example", [Variant("A", 2), Variant("B", 3), Variant("C", 1)])
    ab_testing.add_page(page)
    traffic_split = ab_testing.split_traffic("example")
    assert traffic_split == {"A": 2/6, "B": 3/6, "C": 1/6}
