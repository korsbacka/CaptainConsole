from django.shortcuts import render, redirect

from consoles.models import Console
from .models import Cart


def index(request):
    cart, is_new = Cart.objects.new_or_get(request)
    consoles = cart.consoles.all()
    total = 0
    for x in consoles:
        total += x.console_price
    print(total)
    cart.total = total
    cart.save()
    return render(request, "cart/index.html", {"cart": cart})


def update_cart(request):
    console_id = request.POST.get('console_id')
    if console_id is not None:
        try:
            console = Console.objects.get(id=console_id)
        except Console.DoesNotExist:
            print("product is gone")
            return redirect('cart_index')
        cart, is_new = Cart.objects.new_or_get(request)
        if console in cart.consoles.all():
            cart.consoles.remove(console)
        else:
            cart.consoles.add(console)
        request.session['cart_items'] = cart.consoles.count()
    return redirect(index)
