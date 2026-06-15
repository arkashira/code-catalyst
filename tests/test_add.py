import pytest
from axentx_product import add

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 5, 4),
        (0, 0, 0),
        (3.5, 2.5, 6.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
