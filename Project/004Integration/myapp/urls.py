from django.urls import path
from myapp.views import * 

urlpatterns = [
    path('',index,name='index'),
    path('payment',payment,name='payment'),
    path('email',send_email,name="email")
]