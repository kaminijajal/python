from django.contrib import admin
from app.models import *

# Register your models here.
class EmployeeModel(admin.ModelAdmin):
    list_display =  ['id','name','email','phone','age']
    
admin.site.register(Employee,EmployeeModel)