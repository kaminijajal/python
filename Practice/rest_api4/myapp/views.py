from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *
# Create your views here.

class Emp(APIView):
    
    def get(self,request):
        emps = Employees.objects.all()
        employee = EmployeeSerializer(emps,many=True)
        return Response({"students":employee.data})
    
    def post(self,request):
        emp = EmployeeSerializer(data = request.data)
        if not emp.is_valid():
            return Response({"Error":emp.errors,"message":"Somthing went Wrong..."})
        else:
            emp.save()
            return Response({"data":emp.data,"message":"inserted."})
        
class EmployeeById(APIView):

    def get(self,request,id):
        emp = Employees.objects.get(pk=id)
        ser = EmployeeSerializer(emp)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        emp = Employees.objects.get(pk=id)
        ser = EmployeeSerializer(emp,data=request.data)

        if not ser.is_valid():
            return Response({"Error":ser.error_messages,"messsage":"somthing wrong"})
        else: 
            ser.save()
            return Response({"data":ser.data,"message":"Updated."})
        
    def delete(self,request,id):
        emp = Employees.objects.get(pk=id)
        emp.delete()
        return Response({"messsage":"Deleted"})