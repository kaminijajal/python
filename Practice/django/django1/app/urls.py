from django.urls import path
from app.views import *

urlpatterns = [
    path('',index,name="index"),
    path('add',add,name="add"),
    # path('update',update,name="update"),
    path('delete',delete,name="delete")
]
