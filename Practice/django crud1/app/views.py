from django.shortcuts import render,redirect
from app.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        img = request.FILES['img']

        print(name,email,password,img)
