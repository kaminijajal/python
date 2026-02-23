from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name="index"),
    path('view',view,name="view"),
    path('insert',insert,name="insert"),
    path('delete',delete,name="delete"),
    path('update',update,name="update")
]