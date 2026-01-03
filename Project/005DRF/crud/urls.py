from django.urls import path
from crud.views import * 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("get",get_data,name="index"),
    path("add",add_data,name="add"),
    path("getbyid/<id>",get_data_id,name="getbyid"),
    path("update/<id>",update_data,name="update"),
    path("delete/<id>",delete_data,name="delete")
]

