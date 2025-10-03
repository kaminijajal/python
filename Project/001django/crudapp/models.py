from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    image = models.ImageField(upload_to='profiles',default='test')