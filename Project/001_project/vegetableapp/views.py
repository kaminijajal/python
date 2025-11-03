from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from vegetableapp.models import *

from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request,'index.html')

def allcategories(request):
    categories = Category.objects.all()
    return JsonResponse({"data":list(categories.values())})

def allproducts(request):
    cid = request.GET['catid']
    print(cid)
    if int(cid)==0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=cid)
    return JsonResponse({"data":list(products.values())})

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
    cartdata = Cart.objects.filter(user=request.user)
    return render(request,'shoping-cart.html',{"cdata":cartdata})



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


def add_to_cart(request):
    if not request.user.is_anonymous:
        pid = request.GET['pid']
        product = Product.objects.get(id=pid)


        cdata = Cart.objects.filter(product=product,user=request.user)
        if len(cdata)>0:
            cdata[0].qty = cdata[0].qty+1
            cdata[0].save()
            return HttpResponse("Product alredy exist in cart")
        else:   
            Cart.objects.create(product=product,user=request.user,qty=1)
            return HttpResponse('Product added in cart...........')
    else:
        return HttpResponse(request.user)

def deletecart(request):
    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("cart Deleted.........")

def changeqty(request):
    cartid = request.GET['cartid']
    qty = request.GET['qty']

    cart = Cart.objects.get(pk=cartid)
    if int(qty)<=0:
        cart.delete()
    else:
        cart.qty = qty
        cart.save()
    return HttpResponse("cart updated.........")