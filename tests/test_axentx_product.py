from src.axentx_product.product import Product, get_winning_products

def test_get_winning_products():
    product1 = Product("Product 1", 10)
    product2 = Product("Product 2", 0)
    product3 = Product("Product 3", 5)

    products = [product1, product2, product3]
    winning_products = get_winning_products(products)

    assert len(winning_products) == 2
    assert product1 in winning_products
    assert product3 in winning_products
    assert product2 not in winning_products
