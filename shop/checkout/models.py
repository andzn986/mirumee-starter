from django.db import models


# Create your models here.
class Checkout(models.Model):
    user = models.ForeignKey()
    user_email = models.EmailField(null=False, blank=False)


class CheckoutLine(models.Model):
    variant = models.ForeignKey()
    quantity = models.IntegerField(null=False, blank=False)
    checkout = models.ForeignKey()