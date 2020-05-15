from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='orders_index'),
    path('billing', views.enter_billing, name='billing')
]
