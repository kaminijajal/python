from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cat_img")

    def __str__(self):
        return self.name
    


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    peice = models.FloatField()
    qty = models.IntegerField()
    description=models.TextField()
    image = models.ImageField(upload_to="prod_img")

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def subtotal(self):
        return self.product.peice*self.qty

class Address(models.Model):
    adress = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class UserOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.IntegerField()
    paymentid = models.CharField(max_length=20)
    receiptid= models.CharField(max_length=20)
    orderid = models.CharField(max_length=20)
    date = models.DateField()


class OrderDetails(models.Model):
    order = models.ForeignKey(UserOrder,on_delete=models.CASCADE,related_name="userorder")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()


