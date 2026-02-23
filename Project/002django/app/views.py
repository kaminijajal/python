from django.shortcuts import render,HttpResponse,redirect
from app.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(requset):
    if requset.method == 'POST':
        # print(requset.POST)
        data = requset.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        image = requset.FILES.get('image')
        # print(name,email,phone,age)
        Employee.objects.create(name=name,email=email,phone=phone,age=age,image=image)
    return render(requset,'index.html',{"msg":"Registration Successfully"})

def display(requset):
    emp = Employee.objects.all()
    return render(requset,'display.html',{'employees':emp})

def delete(request):
    eid = request.GET['eid']
    # print(eid)
    emp = Employee.objects.get(pk=eid)
    emp.delete()
    return redirect('display')

def edit(request):
    eid = request.GET['eid']
    # print(eid)
    emp = Employee.objects.get(pk=eid)
    return render(request,"update.html",{"employees":emp})

def update(request):
    if request.method=='POST':
        files = request.FILES
        data = request.POST
        eid = data.get('eid')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        emp = Employee.objects.get(id=eid)
        emp.name= name
        emp.email= email
        emp.phone=phone
        emp.age=age


        if 'image' in files:
            emp.image = files['image']
        emp.save()

        return redirect('display')