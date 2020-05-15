from django.shortcuts import render, redirect, get_object_or_404

from cart.models import Cart
from orders.forms.order_forms import BillingForm, PaymentForm
from orders.models import Order
from orders.forms.guest_form import GuestForm
from user.models import GuestEmail


def index(request):
    cart, cart_is_created = Cart.objects.new_or_get(request)
    order = Order.objects.create(cart=cart)
    if cart_is_created or cart.consoles.count() == 0:
        return redirect("cart_index")

    context = {
        "order": order,
        "cart": cart,
    }
    return render(request, "orders/index.html", context)

