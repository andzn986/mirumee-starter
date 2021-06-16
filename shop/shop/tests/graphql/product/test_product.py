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
    product2 = Product.objects.create(
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

    product_response = content['data']['products']

    assert product_response[0]['description'] == product.description
    assert product_response[0]['price'] == str(product.price)
    assert product_response[0]['quantity'] == product.quantity
    assert product_response[0]['name'] == product.name

    assert product_response[1]['description'] == product2.description
    assert product_response[1]['price'] == str(product2.price)
    assert product_response[1]['quantity'] == product2.quantity
    assert product_response[1]['name'] == product2.name


