from django.shortcuts import render,redirect
from crudapp.models import * 

# Create your views here.
def index(request):
    return render(request, "index.html")

def reg(request):
    if request.method == 'POST':
       data = request.POST
       name = data.get('name') 
       email = data.get('email')
       phone = data.get('phone')
       age = data.get('age')
       img = request.FILES['img']
    #   print(name,email,phone,age)

    Student.objects.create(name=name,email=email,phone=phone,age=age,image=img)
    
    return render(request,"index.html",{"msg":"Registration successfully..... "})

def display(request):
    Students = Student.objects.all()
    return render(request,'display.html',{"students":Students})

def delete(request):
    sid = request.GET['sid']
    st = Student.objects.get(id=sid)
    st.delete()

    return redirect("display")

def update(request):
    sid = request.GET['sid']
    st = Student.objects.get(id=sid)
    return render(request,"update.html",{"student":st})

def edit(request):
    if request.method == 'POST':
        files = request.FILES
        data = request.POST
        sid = data.get('sid')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        st = Student.objects.get(id=sid)
        st.name = name
        st.email = email
        st.phone = phone
        st.age = age

        if 'img' in files:
            st.image = files['img']
            
        st.save()

        return redirect("display")
