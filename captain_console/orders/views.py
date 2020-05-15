from django.shortcuts import render, redirect, get_object_or_404

from cart.models import Cart
from orders.models import Order
from orders.forms.order_forms import BillingProfile, BillingForm


def index(request):
    cart, cart_is_created = Cart.objects.new_or_get(request)
    if cart_is_created or cart.consoles.count() == 0:
        return redirect("cart_index")

    order = Order.objects.new_or_get(request, cart)
    context = {
        "order": order,
        "cart": cart,
    }
    return render(request, "orders/index.html", context)


def enter_billing(request):
    usr = Order.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = BillingForm(data=request.POST)
        if form.is_valid():
            usr = form.save(commit=False)
            usr.user = request.user
            usr.save()
            request['billing'] = form
            return redirect('orders_index')
    return render(request, 'orders/enter_billing.html', {
        'form': BillingForm()
    })



"""
 profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


def enter_billing(request):
    cart, cart_is_created = Cart.objects.new_or_get(request)
    order = Order.objects.new_or_get(request, cart)
    form = BillingForm()
    context = {
        "order": order,
        "cart": cart,
        "form": form,
    }
    return render(request, "orders/enter_billing.html", context)
"""
