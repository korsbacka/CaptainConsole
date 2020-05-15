from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart_index'),
    path('update_cart', views.update_cart, name='update_cart'),
]
