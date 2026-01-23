from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *
# Create your views here.
@api_view(['GET'])
def get_users(request):

    return HttpResponse("GET api calling...")

@api_view(['POST'])
def post_users(request):
    return HttpResponse("POST api calling...")

@api_view(['PUT'])
def put_users(request):
    return HttpResponse("PUT api calling...")

@api_view(['DELETE'])
def delete(request):
    return HttpResponse("DELETE api calling...")

class Student1(APIView):

    def get(self,request):
        allstudents = Student.objects.all()
        students = StudentSerializer(allstudents,many=True)

        return Response({"students":students.data})
    
    def post(self,request):
        # print(request.data)
        data = StudentSerializer(data = request.data)
        if not data.is_valid():
            return Response({"Error":data.errors(),"message":"something wrong...."})
        else:
            data.save()
            return Response({"data":data.data,"messgage":"Data inserted Sucessfully"})
    
    def put(self,request):
        return HttpResponse("put")
    
    def delete(self,request):
        return HttpResponse("delete")
    
class StudentViewById(APIView):

    def get(self,request,id):
        # print(id)
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data)
        if not ser.is_valid():
            return Response({"Error":ser.errors(),"message":"Somthing Wrong.."})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Updated....."})
        
    def patch(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data,partial=True)
        if not ser.is_valid():
            return Response({"Error":ser.errors(),"message":"Somthing Wrong.."})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Updated....."})
        
    def delete(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"Data Deleted....."})

