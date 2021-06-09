import graphene

from .account.authenticate import AuthenticateMutations
from .product.schema import ProductQueries, ProductMutations
from .checkout.schema import CheckoutMutations, CheckoutQueries


class Query(ProductQueries, CheckoutQueries):
    pass


class Mutations(ProductMutations, CheckoutMutations, AuthenticateMutations):
    pass


schema = graphene.Schema(query=Query,mutation=Mutations)
