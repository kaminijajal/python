from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        image  = request.FILES['image']

        # print(id,name,email,phone,age,image)
        if id:
            files = request.FILES
            std = Student.objects.get(id=id)
            std.name = name
            std.email = email
            std.phone = phone
            std.age = age

            if 'image' in files:
                std.image = files['image']

            std.save()
            return render(request,'index.html',{"msg":"Data Updated Successfully..."})
        else:
            Student.objects.create(name=name,email=email,phone=phone,age=age,image=image)
            return render(request,'index.html',{"msg":"Data Insert SuccessFully ......"})

def display(request):
    # sid = request.GET['sid']
    std = Student.objects.all()
    return render(request,'display.html',{'students':std})

def update(request):
    sid = request.GET['sid']
    std = Student.objects.get(id=sid)
    return render(request,'index.html',{"std":std})

def delete(request):
    sid = request.GET['sid']
    std = Student.objects.get(id=sid)
    std.delete()

    return redirect('display')