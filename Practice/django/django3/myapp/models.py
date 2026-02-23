from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to='img',null=True)
