from crudapp.views import *
from django.urls import path

urlpatterns= [
    path('get',get,name="get"),
    path('getbyid/<id>',getbyid,name="getbyid"),
    path('add',add,name="add"),
    path('update/<id>',update,name="update"),
    path('delete/<id>',delete,name="delete")


]