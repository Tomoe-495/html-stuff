from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(User):
	role = models.CharField(max_length=50)

class Product(models.Model):
	name = models.CharField(max_length=80)
	price = models.FloatField()

	def __str__(self):
		return self.name

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	total_price = models.FloatField(default=0)

	def __str__(self):
		return f"user: {self.user} - product: {self.product}"
