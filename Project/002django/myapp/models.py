from django.db import models

# Ceate your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    salary=models.IntegerField()
    phone=models.CharField(max_length=20)
    age=models.IntegerField()
    post=models.CharField(max_length=20)
