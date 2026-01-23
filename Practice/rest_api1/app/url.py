from django.urls import path
from app.views import *

urlpatterns = [
    path("get",get,name="get"),
    path("put",put,name="put"),
    path("post",post,name="post"),
    path("delete",delete,name="delete"),

    path("students",Student1.as_view()),
    path("students/<id>",StudentViewbyId.as_view())

]