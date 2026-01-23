from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from app.models import *
from app.serializar import *

# Create your views here.
@api_view(['GET'])
def get(request):

    return HttpResponse("GET api calling.....")

@api_view(['POST'])
def post(request):
    return HttpResponse("POST api calling.....")

@api_view(['PUT'])
def put(request):
    return HttpResponse("PUT api calling.....")

@api_view(['DELETE'])
def delete(request):
    return HttpResponse("DELETE api calling.....")

class Student1(APIView):

    def get(self,request):
        std = Student.objects.all()
        students = StudentSerializer(std,many=True)

        return Response({"students":students.data})
    
    def post(self,request):
        data = StudentSerializer(data = request.data)
        if not data.is_valid():
            return Response({"Errors":data.errors,"message":"Somthing Went Wrong"})
        else:
            data.save()
            return Response({"Data":data.data,"Message":"Data inserted SuccessFully....."})  
    

class StudentViewbyId(APIView):

    def get(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"Data":ser.data})   
    
    def put(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"Somthing Went Wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Updated....."})   
        
    def delete(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"Data Deleted..."})