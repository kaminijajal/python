from django.shortcuts import render
from rest_framework.response import Response
from crudapp.models import *
from rest_framework.decorators import api_view
from crudapp.serializer import *
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get(requset):
    prod = Product.objects.all()
    ser = ProductSerializer(prod,many=True)
    return Response({"data":ser.data},status=status.HTTP_200_OK)


@api_view(['POST'])  
def add(request):
    prod = ProductSerializer(data=request.data)
    if not prod.is_valid():
        return Response({"error":prod.errors,"msg":"somthig wrong.."},status=status.HTTP_201_CREATED)
    else:
        prod.save()
        return Response({"data":prod.data,"msg":"data inserted..."},status=status.HTTP_200_OK)


@api_view(['GET'])
def getbyid(requeest,id):
    try:
        prod = Product.objects.get(pk=id)
        ser = ProductSerializer(prod)
        return Response({"data": ser.data}, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['PUT'])
def edit(request,id):
    prod = Product.objects.get(pk=id)
    ser = ProductSerializer(prod , data = request.data)
    if not ser.is_valid():
        return Response({"error":ser.errors,"msg":"data not upadated.."}
                        ,status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data":ser.data,"msg":"data updated..."}
                        ,status=status.HTTP_200_OK)    
    

@api_view(['PATCH'])
def singledataedit(request,id):
    prod = Product.objects.get(pk=id)
    ser = ProductSerializer(prod , data = request.data,partial=True)
    if not ser.is_valid():
        return Response({"error":ser.errors,"msg":"data not upadated.."}
                        ,status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data":ser.data,"msg":"data updated..."}
                        ,status=status.HTTP_200_OK) 

@api_view(['DELETE'])
def delete(request,id):
    pro = Product.objects.get(pk=id)
    pro.delete()
    return Response({"data":"data was Deleted.."},status=status.HTTP_200_OK)
