"""AxentX Product – tiny utility library.

Exports a friendly greeting function and a small set of arithmetic helpers.
"""

from .core import greet, add, subtract, multiply, divide

__all__ = [
    "greet",
    "add",
    "subtract",
    "multiply",
    "divide",
]
