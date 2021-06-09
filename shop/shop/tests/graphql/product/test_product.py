from ...product.models import Product


def test_product_by_id(db, client_query):
    product = Product.objects.create(
        name="Test product",
        description="Test product",
        price=10,
        quantity=10
    )

    response = client_query(
        
    )
    pass
