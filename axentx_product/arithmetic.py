"""Basic arithmetic operations with input validation."""

from typing import Union

Number = Union[int, float]


def _validate_number(value: Number, name: str) -> None:
    """Ensure *value* is an int or float; raise TypeError otherwise."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be int or float, got {type(value).__name__}")


def add(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of *a* minus *b*."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return *a* divided by *b*.

    Raises:
        ZeroDivisionError: If *b* is zero.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
