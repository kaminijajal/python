from django.contrib import admin
from crudapp.models import *


# Register your models here.

class StudentModel(admin.ModelAdmin):
    list_display = ['id','name','email','phone','age']

admin.site.register(Student,StudentModel)