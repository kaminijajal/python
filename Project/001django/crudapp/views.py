from django.shortcuts import render,redirect
from crudapp.models import * 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,aauthenticate

# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(requset):
    if requset.method=='POST':
        # print(requset.POST)
        
        data = requset.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        img = requset.FILES['img']
        
        # print(name,email,phone,age)
        Student.objects.create(name=name,email=email,phone=phone,age=age,image=img)
    return render(requset,'index.html',{"msg":"Registration successfully"})

def display(request):
    std = Student.objects.all()
    return render(request,'display.html',{'students':std})

def delete_student(request):
    sid = request.GET['sid']
    # print(sid)
    st = Student.objects.get(id=sid)
    st.delete()
    return redirect("display")

def student_by_id(request):
    sid = request.GET['sid']
    st = Student.objects.get(id=sid)
    return render(request,"update.html",{"student":st})

def updatr_student(request):
    if request.method=='POST':
        data = request.POST
        sid = data.get('sid')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        st = Student.objects.get(id=sid)
        st.name=name
        st.email=email
        st.phone=phone
        st.age=age
        st.save()

        return redirect("display")
    
def user_reg(requset):
    if requset.method=='POST':
        data = requset.POST
        uname = data.get("uname")
        fname = data.get("fname")
        lname = data.get("lname")
        password = data.get("pass")

        user = User(first_name=fname,last_name=lname,username=uname)
        user.set_password(password)
        user.save()
        return render(requset,"reg.html",{"msg":"Registration successfully"})

    return render(requset,'reg.html')

def user_login(requset):
    if requset.method=='POST':
        data = requset.POST
        uname = data.get("uname")
        password = data.get("pass")

        au

    return render(requset,'login.html')