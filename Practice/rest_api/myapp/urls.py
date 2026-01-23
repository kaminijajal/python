from django.urls import path
from myapp.views import *

urlpatterns = [
    path('getusers',get_users,name='getusers'),
    path('postusers',post_users,name="postusers"),
    path('put',put_users,name="put"),
    path('delete',delete,name="delete"),

    path('students/',Student1.as_view()),
    path('students/<id>',StudentViewById.as_view())
]

