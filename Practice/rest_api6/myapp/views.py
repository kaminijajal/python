from django.shortcuts import render , HttpResponse
from rest_framework.decorators import APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *

# from myapp.models import *

# Create your views here.

class CategoryView(APIView):

    def get(request,self):
        cat = Category.objects.all()
        category = CatergorySerializer(cat,many=True)

        return Response({"category":category.data})
    
    def post(self,request):
        cat = CatergorySerializer(data = request.data)

        if not cat.is_valid():
            return Response({"Error":cat.errors,"messsage":"wrong"})
        else:
            cat.save()
            return Response({"data":cat.data,"messsag":"inseted"})
        
class Catergorybyid(APIView):

    def get(self,request,id):
        cat = Category.objects.get(pk=id)
        ser = CatergorySerializer(cat)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        cat = Category.objects.get(pk=id)
        ser = CatergorySerializer(cat,data = request.data)

        if not ser.is_valid():
            return Response({"Error":ser.errors,"message":"wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"messsage":"updated"})
        
    def delete(self,request,id):
        cat = Category.objects.get(pk =id)
        cat.delete()
        return Response({"messsage":"delete"})