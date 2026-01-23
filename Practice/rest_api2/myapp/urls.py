from django.urls import path
from myapp.views import *


urlpatterns = [

        path("get",get,name="get"),
        path("students",Stud.as_view()),
        path("student/<id>",DataViewById.as_view())
]