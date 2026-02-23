from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def add(request):
    if request.method == 'POST':
        data = request.POST
        id= data.get('id')
        name = data.get('name')
        price = data.get('price')
        qty = data.get('qty')
        image  = request.FILES['image']

        # print(name,price,qty,image)
        if id :
            files = request.FILES
            pro = Product.objects.get(id=id)
            pro.name = name 
            pro.price = price
            pro.qty = qty
            if 'image' in files:
                pro.image = files['image']
                
            pro.save()
            messages.success(request, "Data Updated Successfully")
            return render(request,'index.html')
        else:
            Product.objects.create(name=name,price=price,qty=qty,image=image)
            messages.success(request, "Data Add successfully")
            return redirect("index")
   

def display(request):
    pro = Product.objects.all()
    return render(request,'display.html',{"product":pro})

def delete(request):
    pid = request.GET['pid']
    print(pid)
    pro = Product.objects.get(id=pid)
    pro.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("display")

def update(request):
    pid = request.GET['pid']
    pro = Product.objects.get(id=pid)
    return render(request,'index.html',{"pro":pro})