from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from relapp.models import *
from relapp.serializer import *
from rest_framework.response import Response
# Create your views here.

class CategoryView(APIView):

    def get(self,request):
        categories = Category.objects.all()
        ser = CategorySerializer(categories,many=True)
        return Response({"data":ser.data})

class ProductView(APIView):

    def get(self,request):
        products = Product.objects.all()
        ser = ProductSerializer(products,many=True)
        return Response({"data":ser.data})
    
@api_view(["POST"])
def addproduct(request):
    catid = request.GET['category']
    cat = Category.objects.get(pk=catid)
    print(cat)
    request.data['category'] = catid
    ser= ProductSerializer(data = request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"Inserted successfully"})