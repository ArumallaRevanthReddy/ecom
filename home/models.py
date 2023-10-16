from django.db import models
from home.enums import OrderStatus

class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

class Products(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Role(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(verbose_name=("order_status"), max_length=100, choices=OrderStatus.order_status(), default=OrderStatus.ORDERED)
    created_at = models.DateTimeField(auto_now_add=True)

class Order_Products(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

