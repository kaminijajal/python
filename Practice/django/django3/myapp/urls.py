from django.urls import path
from myapp.views import *

urlpatterns =[
    path('',index,name="index"),
    path('addproduct',addproduct,name="addproduct"),
    path('view',view,name="view"),
    path('delete',delete,name="delete"),
    path('update',update,name="update"),
  
]