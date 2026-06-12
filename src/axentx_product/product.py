"""
This module contains the Product class.
"""
class Product:
    def __init__(self, name, price):
        """
        Initialize a Product instance.

        Args:
            name (str): The product's name.
            price (float): The product's price.
        """
        self.name = name
        self.price = price

    def get_price(self):
        """
        Return the product's price.

        Returns:
            float: The product's price.
        """
        return self.price
