from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import *

# Create your views here.

def index(request):
    students = Student.objects.all()
    departments = Department.objects.all()

    std = None  # default
    sid = request.GET.get('sid')  # check if edit clicked
    if sid:
            std = Student.objects.get(id=sid)
       
    return render(request,'index.html',{'std':std,'student':students,'departments': departments})

def add(request):
    if request.method == 'POST':
        data = request.POST

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        department_id = request.POST.get('department')
        image = request.FILES['img']

        # department = Department.objects.get(id=department_id)
        # print(name,email,phone,age,image,department_id)
        sid = data.get('sid')
        if sid:
            files = request.FILES
            std = Student.objects.get(id=sid)
            std.name = name
            std.email = email
            std.phone = phone
            std.age = age
            std.department_id = department_id
            if 'img' in files:
                std.image = files['img']
            
            std.save()
            messages.success(request, "Student updated successfully!")
        else:
            Student.objects.create(name=name,email=email,phone=phone,age=age,image=image,department_id=department_id)
            messages.success(request, "Registration successfully......")
    return redirect('index')

def delete(request):
    id = request.GET['sid']
    # print(id)
    std = Student.objects.get(id=id)
    std.delete()
    messages.success(request, "Data Delete Successfully......")
    return redirect('index')


