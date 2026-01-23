from django.urls import path
from myapp.views import *
urlpatterns = [
    path('get',get,name='get'),

    path('students',Std.as_view()),
    path('students/<id>',StdViewId.as_view())
]