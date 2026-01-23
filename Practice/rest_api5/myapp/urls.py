from django.urls import path
from myapp.views import *

urlpatterns = [
    
    path("prod",ProductView.as_view()),
    path("prod/<id>",ProductById.as_view())
]
