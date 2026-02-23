from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    # std = Students.objects.all()
    return render(request,"index.html")

def insert(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('pass')
        age = data.get('age')
        city = data.get('city')
        gender = data.get('gender')
        hobbies = data.getlist('hobbies')
        hobbies1 = (',').join(hobbies)
        address = data.get('address')
        image = request.FILES['image']

        print(name,email,password,age,city,gender,hobbies1,address,image)
    Students.objects.create(name=name,email=email,password=password,age=age,city=city,gender=gender,hobbies=hobbies1,address=address,image=image)
    messages.success(request, "Registration Successfully ....")
    return redirect('index')

def display(request):
    std = Students.objects.all()
    return render(request,"display.html",{"student":std})


def delete(request):
    sid = request.GET['sid']
    st = Students.objects.get(id=sid)
    # print(st)
    st.delete()
    messages.success(request, "Data Deleted Successfully ....")
    return redirect('display')

def update(request):
    sid = request.GET.get('sid')
    std  = Students.objects.get(id=sid)
    if request.method=='POST':
        files = request.FILES
        data  = request.POST

        name = data.get('name')
        email = data.get('email')
        password = data.get('pass')
        age = data.get('age')
        city = data.get('city')
        gender = data.get('gender')
        hobbies = data.getlist('hobbies')
        std.hobbies = ",".join(hobbies)
        address = data.get('address')
        image = files.get('image')


        std.name=name
        std.email = email
        std.password = password
        std.age = age
        std.city = city
        std.gender = gender
        std.hobbies = hobbies
        std.address = address

        if 'image' in files:
            std.image = files['image']

        print(name,email,password,age,city,gender,hobbies,address,image)
    return render(request,"update.html",{'std':std})
