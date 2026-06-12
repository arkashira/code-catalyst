import pytest
from axentx_product import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-5, 5, 0),
        (3.5, 2.5, 6.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-1, 5, -5),
        (2.5, 4, 10.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2.0),
        (5, 2, 2.5),
        (-8, -2, 4.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize(
    "func,invalid",
    [
        (add, "a"),
        (subtract, None),
        (multiply, [1, 2]),
        (divide, {"x": 1}),
    ],
)
def test_type_validation(func, invalid):
    with pytest.raises(TypeError):
        func(invalid, 1)
    with pytest.raises(TypeError):
        func(1, invalid)
