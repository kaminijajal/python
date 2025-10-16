from django.contrib import admin
from vegetableapp.models import *

# Register your models here.
class CategoryModel(admin.ModelAdmin):
    list_display=['id','name','image']

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','peice','qty','image','category']



admin.site.register(Category,CategoryModel)
admin.site.register(Product,ProductModel)
admin.site.register(Cart)



