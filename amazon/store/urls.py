from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("auth/", views.auth, name="auth"),
	path("auth/register/", views.register, name="register"),
	path("auth/login/", views.login_user, name="login"),
	path("auth/logout/", views.logout_user, name="logout"),
	path("auth/delete/user/<int:id>", views.delete_user, name="delete_user"),
	path("auth/delete/product/<int:id>", views.delete_prod, name="delete_prod"),
	path("auth/delete/cart/<int:id>", views.delete_cart, name="delete_cart"),
	path("product/add", views.add_prod, name="add_prod"),
	path("product/add/cart/<int:id>", views.add_to_cart, name="add_cart"),
	path("cart/", views.cart, name="cart")
]