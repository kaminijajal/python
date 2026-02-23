from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def add(request):
    if request.method == "POST":
        data = request.POST
        sid= data.get('id')
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")
        image = request.FILES['image']
        print(name,email,phone,age,image)

        if sid:
            files = request.FILES
            std = Student.objects.get(id=int(sid))
            std.name = name
            std.email = email
            std.phone = phone
            std.age = age
            if 'image' in files:
                std.image = files['image']   

            std.save()     
           
            messages.success(request, "Data Updated Successfully ✅")
            return render(request,'view.html')
        else:
            Student.objects.create(name=name,email=email,phone=phone,age=age,image=image)
            messages.success(request, "Data inserted successfully ✅")
            return redirect('index')   

def view(request):
    std = Student.objects.all()
    return render(request,"view.html",{"students":std})

def delete(request):
    sid = request.GET['sid']
    print(sid)
    std = Student.objects.get(id=sid)
    std.delete()
    messages.success(request, "Data Deleted successfully ✅")
    return redirect("view")

def update(request):
    sid = request.GET['sid']
    print(sid)
    std = Student.objects.get(id=sid)
    return render(request,'index.html',{"std":std})

