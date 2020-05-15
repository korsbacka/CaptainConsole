from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


from cart.models import Cart

User = settings.AUTH_USER_MODEL


class OrderManager(models.Manager):
    def new_or_get(self, request, cart):
        order_id = request.session.get("order_id", None)
        query = self.get_queryset().filter(id=order_id)
        if query.count() == 1:
            new_order = False
            order = query.first()
            if request.user.is_authenticated and order.user is None:
                order.user = request.user
                order.save()
        else:
            order = self.new_order(user=request.user, cart=cart)
            new_order = True
            request.session['order_id'] = order.id
        return cart, new_order

    def new_order(self, user=None, cart=None):
        user_auth = None
        if user is not None:
            if user.is_authenticated:
                user_auth = user
        return self.model.objects.create(user=user_auth, cart=cart)

"""
class OrderManager(models.Manager):
    def new_or_get(self, cart_):
        qs = self.get_queryset().filter(cart=cart_, active=True)
        if qs.count() == 1:
            created = False
            obj = qs.first()
        else:
            obj = self.model.objects.create(cart=cart_)
            created = True
        return obj
"""


class BillingProfile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    card_holder = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=255)
    cvc_number = models.CharField(max_length=255)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    order_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)
    billing = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)
