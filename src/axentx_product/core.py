"""Core utilities for the axentx_product package."""

from typing import Union

Number = Union[int, float]


def greet(name: str) -> str:
    """
    Return a friendly greeting.

    Parameters
    ----------
    name: str
        The name to greet.

    Returns
    -------
    str
        A greeting string in the form ``"Hello, <name>!"``.
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return f"Hello, {name}!"


def add(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of *a* minus *b*."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the quotient of *a* divided by *b*.

    Raises
    ------
    ZeroDivisionError
        If *b* is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
