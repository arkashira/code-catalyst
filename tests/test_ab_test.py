import pytest
from ab_test import ABTest, Variant

def test_split_traffic():
    variant1 = Variant('https://example.com/variant1')
    variant2 = Variant('https://example.com/variant2')
    ab_test = ABTest(variant1, variant2)
    result = ab_test.split_traffic()
    assert result == (variant1, variant2)

def test_update_results():
    variant1 = Variant('https://example.com/variant1')
    variant2 = Variant('https://example.com/variant2')
    ab_test = ABTest(variant1, variant2)
    ab_test.update_results(variant1, True, True)
    assert variant1.clicks == 1
    assert variant1.conversions == 1
    ab_test.update_results(variant2, True, False)
    assert variant2.clicks == 1
    assert variant2.conversions == 0

def test_get_results():
    variant1 = Variant('https://example.com/variant1')
    variant2 = Variant('https://example.com/variant2')
    ab_test = ABTest(variant1, variant2)
    ab_test.update_results(variant1, True, True)
    ab_test.update_results(variant2, True, False)
    result = ab_test.get_results()
    assert result['variant1']['url'] == 'https://example.com/variant1'
    assert result['variant1']['clicks'] == 1
    assert result['variant1']['conversions'] == 1
    assert result['variant1']['ctr'] == 0.5
    assert result['variant1']['conversion_rate'] == 1.0
    assert result['variant2']['url'] == 'https://example.com/variant2'
    assert result['variant2']['clicks'] == 1
    assert result['variant2']['conversions'] == 0
    assert result['variant2']['ctr'] == 0.5
    assert result['variant2']['conversion_rate'] == 0.0

def test_get_results_zero_clicks():
    variant1 = Variant('https://example.com/variant1')
    variant2 = Variant('https://example.com/variant2')
    ab_test = ABTest(variant1, variant2)
    result = ab_test.get_results()
    assert result['variant1']['ctr'] == 0.0
    assert result['variant1']['conversion_rate'] == 0.0
    assert result['variant2']['ctr'] == 0.0
    assert result['variant2']['conversion_rate'] == 0.0
