def validate_product(product):
    if product.price <= 0:
        raise ValueError("Price must be greater than zero")
    return True
