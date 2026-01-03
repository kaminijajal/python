from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView,permission_classes
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *
from rest_framework.permissions import IsAuthenticated
from myapp.permissions import *

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    return HttpResponse("Get Api Calling.....")

@api_view(['POST'])
@permission_classes([isAdminUserOnly])
def post_user(request):
    return HttpResponse("Post Api Calling.....")

@api_view(['PUT'])
def put_user(request):
    return HttpResponse("Put Api Calling.....")

@api_view(['DELETE'])
def delete_user(request):
    return HttpResponse("Delete Api Calling.....")


class StudentView(APIView):

    def get(self,request):
        allstudents = Student.objects.all()
        students = StudentSerializer(allstudents,many=True)
        return Response({"students":students.data})
    
    def post(self,request):
        data = StudentSerializer(data = request.data)
        if not data.is_valid():
            return Response({"Errors":data.errors(),"message":"Somthing Went Wrong"})
        else:
            data.save()
            return Response({"data":data.data,"message":"Data insert Sucreesfully...."})
        
    
class StudentViewId(APIView):
    def get(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student)    
        return Response({"data":ser.data})
    
    def put(self,request,id):
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,data=request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors(),"message":"Somthing went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"data Successfully Updated..."})

    def delete(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"message":"Data Deleted...."})