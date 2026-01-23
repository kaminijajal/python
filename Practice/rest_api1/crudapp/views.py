from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crudapp.serializer import *
from crudapp.models import *
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get(request):
    try:
        emp = Employee.objects.all()
        ser = EmployeeSerializer(emp,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getbyid(request,id):
    try:
        emp = Employee.objects.get(pk=id)
        ser = EmployeeSerializer(emp)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    
    except Employee.DoesNotExist:
        return Response(
            {"message": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def add(request):
    try:
        emp = EmployeeSerializer(data = request.data)
        if not emp.is_valid():
            return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)
        else:
            emp.save()
            return Response({"data":emp.data,"messsage":"Data inserted.."},status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request,id):
    try:
        emp = Employee.objects.get(pk=id)
        ser = EmployeeSerializer(emp,data = request.data)
        if not ser.is_valid():
            return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data Updated.."},status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(
            {"message": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,id):
    try:
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({"message":"data Deleted.."},status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(
            {"message": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)