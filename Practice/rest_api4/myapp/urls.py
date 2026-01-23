from django.urls import path
from myapp.views import *
urlpatterns = [

    path("employee",Emp.as_view()),
    path("employee/<id>",EmployeeById.as_view())
]