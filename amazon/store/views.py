from django.shortcuts import render, redirect
from .models import User, Product, Cart
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request, "home.html", {"products":products})

def auth(request):
	users = User.objects.all()
	user = request.user
	return render(request, "auth.html", {"users":users, "user":user})

@login_required(login_url="login")
def add_to_cart(request, id):
	prod = Product.objects.get(id=id)
	user = User.objects.get(id=request.user.id)
	try:
		cart = Cart.objects.get(user=user, product=prod)
		cart.quantity = cart.quantity + 1
		cart.total_price = float(str(cart.quantity * prod.price)[0:5])
	except:
		cart = Cart(user=user, product=prod, total_price=prod.price)
	cart.save()
	return redirect("home")

def delete_cart(request, id):
	cart = Cart.objects.get(id=id)
	cart.delete()
	return redirect("cart")

@login_required(login_url="login")
def cart(request):
	carts = Cart.objects.filter(user=request.user)
	total_sum = 0
	for cart in carts:
		total_sum += cart.total_price
	total_sum = float(str(total_sum)[0:5])
	return render(request, "cart.html", {"carts":carts, "total_sum":total_sum})

def delete_user(request, id):
	user = User.objects.get(id=id)
	user.delete()
	return redirect("auth")

def delete_prod(request, id):
	prod = Product.objects.get(id=id)
	prod.delete()
	return redirect("home")

def register(request):
	error = ""
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		role = request.POST["role"]
		try:
			user = User.objects.get(username=username)
			error = f"a user with this username[{username}] already exists"
		except:
			user = User.objects.create_user(username=username, password=password)
			user.role = role
			user.save()
			return redirect("auth")
	return render(request, "register.html", {"error":error})

def login_user(request):
	if request.user.is_authenticated:
		return redirect("home")
	error = ""
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("home")
		error = "this user doesn't exists"
	return render(request, "login.html", {"error":error})

@login_required(login_url="login")
def add_prod(request):
	error = ""
	if request.method == "POST":
		name = request.POST["name"]
		price = request.POST["price"]
		try:
			prod = Product.objects.get(name=name)
			error = "this product already exists"
		except:
			prod = Product(name=name,price=price)
			prod.save()
			return redirect("home")
	return render(request, "add_prod.html")

@login_required(login_url="home")
def logout_user(request):
	logout(request)
	return redirect("home")
