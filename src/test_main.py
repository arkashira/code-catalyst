import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(4, 2) == 2
    assert divide(-4, 2) == -2
    assert divide(-4, -2) == 2
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
