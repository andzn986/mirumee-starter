from decimal import Decimal
import pytest
from graphene_django.utils.testing import graphql_query
from ..product.models import Product, ProductVariant


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.fixture
def product():
    product = Product.objects.create(
        name="test",
        description="",
        price=Decimal("10.00"),
        quantity=10.00
    )
    return product


@pytest.fixture
def variant(my_product):
    variant = ProductVariant.objects.create(
        product=my_product,
        name="variant",
        sku="my-variant",
        price=Decimal("10.00")
    )
    return variant
