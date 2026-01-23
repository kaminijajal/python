from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.serializer import *
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get(request):
    return HttpResponse("hello")

class Std(APIView):
    def get(request,self):
        stud = Student.objects.all()
        students = StudentSerializer(stud,many=True)
        return Response({"students":students.data})

    def post(self,request):
        std = StudentSerializer(data = request.data)
        if not std.is_valid():
            return Response({"Errors":std.errors,"message":"Wrong.."})
        else:
            std.save()
            return Response({"data":std.data,"message":"Inserted...."})
        
class StdViewId(APIView):
    
    def get(self,request,id):
        std = Student.objects.get(pk=id)
        ser = StudentSerializer(std)
        return Response({"data":ser.data})
    
    def put(self,request,id):
        std = Student.objects.get(pk=id)
        ser = StudentSerializer(std,data = request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"message":"Wrong.."})
        else:
            ser.save()
            return Response({"data":ser.data,"messsage":"Updated.."})
        
    def delete(self,request,id):
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({"message":"deleted..."})

