from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"add.html")

def addproduct(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image = request.FILES['image']

        print(name,description,price,image)
        Product.objects.create(name=name,description=description,price=price,image=image)
    
        return render(request,'add.html',{"msg":'Product added....'})
    return render(request,'add.html')


def view(request):
    pro = Product.objects.all()
    
    return render(request,'view.html',{'products':pro})

def delete(request):
    pid = request.GET['pid']
    pro = Product.objects.get(id=pid)
    pro.delete()
    return redirect('view')

def update(request):
    if request.method=='POST':
        files = request.FILES
        data = request.POST
        pid = data.get('pid')
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        pro = Product.objects.get(id=pid)
        pro.name = name
        pro.description = description
        pro.price = price
        
        if 'image' in files:
            pro.image = files['image']

        pro.save()
        return redirect('view')

    pid = request.GET['pid']    
    pro = Product.objects.get(id=pid)
    return render(request,'update.html',{'pro':pro})
        





