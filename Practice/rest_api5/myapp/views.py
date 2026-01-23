from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serializer import *

from rest_framework.response import Response
# Create your views here.

class ProductView(APIView):

    def get(request,self):
        pro = Product.objects.all()
        product = ProductSerializer(pro,many=True)
        return Response({"products":product.data})
    
    def post(self,request):
        product = ProductSerializer(data = request.data)
        if not product.is_valid():
            return Response({"Error":product.errors,"message":"wrong"})
        else:
            product.save()
            return Response({"data":product.data,"messsage":"inserted."})

class ProductById(APIView):
    
    def get(self,request,id):
        product =Product.objects.get(pk=id)
        
        ser = ProductSerializer(product)
        print(ser)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        product = Product.objects.get(pk=id)
        ser = ProductSerializer(product,data = request.data)

        if not ser.is_valid():
            return Response({"Error":ser.errors,"messsage":"wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"updated."})
        
    def delete(self,request,id):
        product = Product.objects.get(pk=id)
        product.delete()
        return Response({"messsage":"deleted."})