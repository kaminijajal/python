from django.urls import path
from myapp.views import *


urlpatterns = [
    
    path ("getusers",get_users,name="getusers"),
    path("postuser",post_user,name="postuser"),
    path("putuser",put_user,name="putuser"),
    path("deleteusers",delete_user,name="deleteusers"),

    path("students/",StudentView.as_view()),
    path("students/<id>",StudentViewId.as_view())
]
