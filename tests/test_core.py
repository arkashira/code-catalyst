import pytest
from axentx_product import greet, add, subtract, multiply, divide

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"

def test_greet_type_error():
    with pytest.raises(TypeError):
        greet(123)

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0.5, 0.25, 0.75),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (2.5, 0.5, 2.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0.5, 4, 2.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
