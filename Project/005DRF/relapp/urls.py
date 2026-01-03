from django.urls import path
from relapp.views import *


urlpatterns = [
    path("categories",CategoryView.as_view()),
    path("products",ProductView.as_view()),

    path("addproduct",addproduct,name="addproduct")
]