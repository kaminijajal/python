from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to='img',default='test')

class test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()