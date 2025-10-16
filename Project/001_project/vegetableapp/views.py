from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vegetableapp.models import *


# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    try:
        cid = int(request.GET['cid'])
        # print(cid)
        # categories = Category.objects.all()
        if cid!= 0:
            products = Product.objects.filter(category_id=cid)
        else:
            products = Product.objects.all()
        return render(request,'index.html',{"categories":categories,
                    "products": products})
    except Exception as e:
        return render(request,'index.html',{"categories":categories,
                    "products": products})

def blog_details(request):
    return render(request,'blog-details.html')

def blog(request):
    return render(request,'blog.html')

@login_required(login_url="login")
def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def main(request):
    return render(request,'main.html')

def shope_details(request):
    return render(request,'shop-details.html')

def shop_grid(request):
    return render(request,'shop-grid.html')

@login_required(login_url="login")
def shopping_cart(request):
    return render(request,'shoping-cart.html')



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).exists()
        if user:
            return render(request,'login.html',{"rerr":"Username Already Exists"})
        u = User(username=username,email=email)
        u.set_password(password)
        u.save()
        return render(request,'login.html',{"msg":"User Registered Successfully"})
    return render(request,'login.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,"index.html")
        else:
            return render(request,"login.html",{"err":"Invalid Username or Password"})
            
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("index")

@login_required(login_url="login")
def add_to_cart(request):
    pid = request.GET['pid']
    product = Product.objects.get(id=pid)
    Cart.objects.create(product=product,user=request.user,qty=1)
    return redirect('index')