"""
axentx_product – a minimal arithmetic utility library.

Provides simple, well‑tested functions for addition, subtraction,
multiplication and division. All operations validate their inputs
and raise clear exceptions on error.
"""

from .arithmetic import add, subtract, multiply, divide

__all__ = ["add", "subtract", "multiply", "divide"]
