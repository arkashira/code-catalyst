from src.axentx_product.product import Product
from src.axentx_product.validation import validate_product

def test_product_creation():
    product = Product("Test Product", 10.99)
    assert product.name == "Test Product"
    assert product.price == 10.99

def test_get_price():
    product = Product("Test Product", 10.99)
    assert product.get_price() == 10.99

def test_validation():
    product = Product("Test Product", 10.99)
    assert validate_product(product) is True

def test_validation_failure():
    product = Product("Test Product", -1.00)
    try:
        validate_product(product)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Price must be greater than zero"
