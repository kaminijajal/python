from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *

# Create your views here.
# 
# @api_view(['GET'])
# def index(request):
#     return render(request,'index.html')

@api_view(['GET'])
def get(request):
    return HttpResponse("Get api Calling....")

class Stud(APIView):

    def get(request,self):
        std = Student.objects.all()
        students = StudentSerializer(std,many=True)
        return Response({"student":students.data})
    
    def post(self,request):
        data = StudentSerializer(data = request.data)
        if not data.is_valid():
            return Response({"Errors":data.errors,"message":"Somthing Wrong..."})
        else:
            data.save()
            return Response({"Data":data.data,"message":"Data inserted....."})

class DataViewById(APIView):

    def get(self,request,id):
        stud = Student.objects.get(pk=id)
        ser = StudentSerializer(stud)
        return Response({"Data":ser.data})
    
    def put(self,request,id):
        Stud = Student.objects.get(pk=id)
        ser = StudentSerializer(Stud,data = request.data)

        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"Somthing Wrong.."})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Updated..."})
        
    def delete(self,request,id):
        Stud = Student.objects.get(pk=id)
        Stud.delete()
        return Response({"message":"Data Deleted..."})

