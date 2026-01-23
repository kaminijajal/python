from django.urls import path
from myapp.views import *

urlpatterns = [
    path("category",CategoryView.as_view()),
    path("category/<id>",Catergorybyid.as_view())
]