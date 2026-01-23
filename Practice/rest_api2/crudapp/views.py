from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from crudapp.models import *
from crudapp.serializer import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get(request):
    try:
        pro = Product.objects.all()
        ser = ProductSerializer(pro,many=True)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getbyid(request,id):
    try:
        pro = Product.objects.get(pk=id)
        ser = ProductSerializer(pro)
        return Response({"data":ser.data},status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add(request):
    try:
        pro = ProductSerializer(data=request.data)
        if not pro.is_valid():
             return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)
        else:
            pro.save()
            return Response({"data":pro.data,"message":"Data inserted.."},status=status.HTTP_201_CREATED)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request,id):
    try:
        pro = Product.objects.get(pk=id)
        ser = ProductSerializer(pro,data = request.data)
        if not ser.is_valid():
            return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)
        else:
            ser.save()
            return Response({"data":ser.data,"messsage":"data updated"},status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,id):
    try:
        pro =  Product.objects.get(pk=id)
        pro.delete()
        return Response({"message":"data Deleted.."},status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"message":"Somthing went Wrong...."},status=status.HTTP_400_BAD_REQUEST)

