from crudapp.views import *
from django.urls import path

urlpatterns = [
    path("get",get,name="get"),
    path('add',add,name='add'),
    path('getbyid/<id>',getbyid,name='getbyid'),
    path('edit/<id>',edit,name="edit"),
    path('delete/<id>',delete,name="delete"),
    path('singledataedit/<id>',singledataedit,name="singledataedit")

]