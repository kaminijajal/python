from django.urls import path
from myapp.views import * 

urlpatterns = [

    path('', index, name='home'),  
    path('payment',payment,name='payment')

]