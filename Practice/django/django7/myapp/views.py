from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def insert(request):
    if request.method == "POST":
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        image = request.FILES['image']

        print(name,image)
        if id:
            files = request.FILES
            cat = Category.objects.get(id=id)
            cat.name = name
            
            if 'image' in files:
                cat.image = files['image']

            print(cat.name,cat.image)
            cat.save()
            messages.success(request,"Category Update successfully!")
            return redirect('view')    
        else:    
            Category.objects.create(name=name,image=image)
            messages.success(request,"Category added successfully!")
            return redirect('index')

def view(request):
    cat =Category.objects.all()
    return render(request,"view.html",{"cats":cat})

def delete(request):
    cid = request.GET['cid']
    print(cid)
    cat = Category.objects.get(id=cid)
    cat.delete()
    messages.success(request,"Category Deleted successfully!")
    return redirect('view')

def update(request):
    cid = request.GET['cid']
    print(cid)
    cat = Category.objects.get(id=cid)
    return render(request,'index.html',{"cat":cat})