from .portfolio import Portfolio
from .product import Product

class ChainPlaybook:
    def __init__(self):
        self.portfolio = Portfolio()

    def add_product_to_portfolio(self, product):
        self.portfolio.add_product(product)

    def get_portfolio_products(self):
        return self.portfolio.get_products()
