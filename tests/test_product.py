"""
This module contains unit tests for the Product class.
"""
from axentx_product.product import Product

def test_product_init():
    """
    Test the Product class's __init__ method.
    """
    product = Product('Test Product', 9.99)
    assert product.name == 'Test Product'
    assert product.price == 9.99

def test_product_get_price():
    """
    Test the Product class's get_price method.
    """
    product = Product('Test Product', 9.99)
    assert product.get_price() == 9.99
