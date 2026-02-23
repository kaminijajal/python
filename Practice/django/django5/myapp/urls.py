from django.urls import path
from myapp.views import *
urlpatterns = [
    path('',index,name="index"),
    path('add',add,name="add"),
    path('delete',delete,name="delete"),
    path('update',update,name="update"),
    path('display',display,name="display")
]