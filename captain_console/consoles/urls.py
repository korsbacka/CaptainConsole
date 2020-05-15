from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='consoles_index'),
    path('<int:id>', views.get_console_by_id, name="console_details"),
    path('search/', views.search, name='search'),
]
