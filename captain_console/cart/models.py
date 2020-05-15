from django.db import models
from django.conf import settings
from consoles.models import Console

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        query = self.get_queryset().filter(id=cart_id)
        if query.count() == 1:
            new_cart = False
            cart = query.first()
            if request.user.is_authenticated and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            cart = self.new_cart(user=request.user)
            new_cart = True
            request.session['cart_id'] = cart.id
        return cart, new_cart

    def new_cart(self, user=None):
        user_auth = None
        if user is not None:
            if user.is_authenticated:
                user_auth = user
        return self.model.objects.create(user=user_auth)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    consoles = models.ManyToManyField(Console, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
