from ab_test import ABTest, Variant

def test_split_traffic():
    variant1 = Variant("Variant 1", 50)
    variant2 = Variant("Variant 2", 50)
    ab_test = ABTest(variant1, variant2)
    results = [ab_test.split_traffic() for _ in range(10000)]
    assert abs(results.count("Variant 1") / len(results) - 0.5) < 0.01

def test_record_engagement():
    variant1 = Variant("Variant 1", 50)
    variant2 = Variant("Variant 2", 50)
    ab_test = ABTest(variant1, variant2)
    ab_test.record_engagement("Variant 1")
    ab_test.record_engagement("Variant 2")
    assert ab_test.get_results() == {"Variant 1": 1, "Variant 2": 1}

def test_get_statistical_significance():
    variant1 = Variant("Variant 1", 50)
    variant2 = Variant("Variant 2", 50)
    ab_test = ABTest(variant1, variant2)
    for _ in range(1000):
        ab_test.record_engagement("Variant 1")
    for _ in range(100):
        ab_test.record_engagement("Variant 2")
    assert "Statistically significant difference" in ab_test.get_statistical_significance()
