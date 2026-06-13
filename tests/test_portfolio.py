from src.axentx_product.portfolio import Portfolio
from src.axentx_product.product import Product

def test_portfolio():
    portfolio = Portfolio()
    product1 = Product("Product 1", 10)
    product2 = Product("Product 2", 0)

    portfolio.add_product(product1)
    portfolio.add_product(product2)

    products = portfolio.get_products()

    assert len(products) == 2
    assert product1 in products
    assert product2 in products
