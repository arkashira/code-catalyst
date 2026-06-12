import os
import json
import pytest
import random
from ab_test import ABTest, DATA_FILE

@pytest.fixture(autouse=True)
def clean_dashboard(tmp_path):
    # Ensure dashboard file is removed before each test
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    yield
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def simulate(test: ABTest, variation: str, impressions: int, conversion_rate: float):
    for _ in range(impressions):
        converted = random.random() < conversion_rate
        test.record_impression(variation, converted)

def test_variation_limit():
    test = ABTest("test1")
    test.add_variation("A")
    test.add_variation("B")
    test.add_variation("C")
    with pytest.raises(ValueError):
        test.add_variation("D")

def test_start_stop_and_dashboard():
    test = ABTest("demo")
    test.add_variation("A")
    test.add_variation("B")
    test.start()
    simulate(test, "A", 1000, 0.10)
    simulate(test, "B", 1000, 0.12)
    test.stop()
    assert os.path.exists(DATA_FILE)
    with open(DATA_FILE) as f:
        data = json.load(f)
    assert "demo" in data
    res = data["demo"]
    assert "A" in res and "B" in res
    assert res["A"]["impressions"] == 1000
    assert res["B"]["impressions"] == 1000
    assert res["B"]["significant_vs_control"] in (True, False)

def test_significance_detection():
    test = ABTest("sig_test")
    test.add_variation("A")
    test.add_variation("B")
    test.start()
    # A: 10% conversion, B: 20% conversion
    simulate(test, "A", 2000, 0.10)
    simulate(test, "B", 2000, 0.20)
    test.stop()
    with open(DATA_FILE) as f:
        data = json.load(f)
    res = data["sig_test"]
    assert res["B"]["significant_vs_control"] is True

def test_no_impressions():
    test = ABTest("empty")
    test.add_variation("A")
    test.add_variation("B")
    test.start()
    # only A gets impressions
    simulate(test, "A", 500, 0.15)
    test.stop()
    with open(DATA_FILE) as f:
        data = json.load(f)
    res = data["empty"]
    assert res["B"]["impressions"] == 0
    assert res["B"]["conversion_rate"] == 0.0
    assert res["B"]["p_value_vs_control"] == 1.0
