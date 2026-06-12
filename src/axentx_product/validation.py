def validate_product(product):
    if product.price <= 0:
        raise ValueError("Product price must be greater than zero")
    return True
