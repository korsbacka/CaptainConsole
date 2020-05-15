from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from cart.models import Cart


class BillingDetails(models.Model):
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.IntegerField(validators=[MaxLengthValidator(1), MinLengthValidator(5)])
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.IntegerField(validators=[MaxLengthValidator(3), MinLengthValidator(3)])


class PaymentDetails(models.Model):
    card_holder = models.CharField(max_length=255)
    card_number = models.IntegerField(validators=[MaxLengthValidator(16), MinLengthValidator(16)])
    expiry_date = models.CharField(max_length=255)
    cvc_number = models.IntegerField(validators=[MaxLengthValidator(3), MinLengthValidator(3)])


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    order_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)
    payment = models.ForeignKey(PaymentDetails, null=True, blank=True, on_delete=models.CASCADE)
    billing = models.ForeignKey(BillingDetails, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
