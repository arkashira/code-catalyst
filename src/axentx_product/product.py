class Product:
    def __init__(self, name, demand_score):
        self.name = name
        self.demand_score = demand_score

    def __repr__(self):
        return f"Product('{self.name}', {self.demand_score})"

def get_winning_products(products):
    winning_products = []
    for product in products:
        if product.demand_score > 0:
            winning_products.append(product)
    return winning_products
