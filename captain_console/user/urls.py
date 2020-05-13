from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register_user'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login_user'),
    path('logout', LogoutView.as_view(next_page='login_user'), name='logout_user'),
    path('profile', views.profile, name="profile"),
]
