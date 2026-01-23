from django.urls import path
from crudapp.views import *

urlpatterns = [
    path("get",get,name="get"),
    path("getbyid/<id>",getbyid,name="getbyid"),
    path("add",add,name="add"),
    path("update/<id>",update,name="update"),
    path("delete/<id>",delete,name="delete")
]