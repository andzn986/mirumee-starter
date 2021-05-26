from django.db import models
from ..product.models import ProductVariant, Product


# Create your models here.
class Checkout(models.Model):
    user = models.ForeignKey()
    user_email = models.EmailFIeld()


class CheckoutLine(models.Model):
    variant = models.ForeignKey()
    quantity = models.IntegerField()
    checkout = models.ForeignKey()
