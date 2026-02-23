from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=5)
    age = models.IntegerField()
    city = models.CharField()
    gender = models.CharField(null=True)
    hobbies = models.CharField(null=True)
    address = models.TextField()
    image = models.ImageField(upload_to='img',null=True,blank=True)
 