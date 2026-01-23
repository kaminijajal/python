from django.db import models
# from myapp.views import *
# Create your models here.
class Employees(models.Model):
    ename = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()