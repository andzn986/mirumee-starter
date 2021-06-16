from ....product.models import Product
import json
from decimal import Decimal


def test_product_by_id(db, client_query):
    product = Product.objects.create(
        name="Test Product",
        description="Product description",
        price=Decimal("10.00"),
        quantity=10.00
    )

    response = client_query(
        """
        query myproduct($id: ID!) {
            product(id: $id){
                price
                id
                name
                description
                quantity
            }
        }
        """,
        variables={'id': 1}
    )
    content = json.loads(response.content)

    product_response = content['data']['product']

    assert product_response['id'] == str(product.id)
    assert product_response['description'] == product.description
    assert product_response['quantity'] == product.quantity
    assert product_response['price'] == str(product.price)


def test_product_list(db, client_query):
    product = Product.objects.create(
        name="test1",
        description="test1",
        price=Decimal("10.00"),
        quantity=10.00
    )
    product = Product.objects.create(
        name="test2",
        description="test2",
        price=Decimal("20.00"),
        quantity=15.00
    )

    response = client_query(
        """
        query{
            products{
                name
                description
                price
                quantity
            }
        }
        """,
    )
    content = json.loads(response.content)

    products_response = content['data']

    assert products_response['description'] == product.description
    assert products_response['price'] == str(product.price)
    assert products_response['quantity'] == product.quantity
