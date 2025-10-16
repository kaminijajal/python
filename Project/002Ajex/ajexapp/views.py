from django.shortcuts import render,HttpResponse
from ajexapp.models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    # print("search calling....")
    data = request.GET['data']
    # products = Product.objects.filter(name=data)
    # print(products)
    # print(data)
    # return HttpResponse("done")
    # products = Product.objects.filter(name=data)
    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"data":list(products.values())})

def countries(request):
    allcountries = Country.objects.all()
    return JsonResponse({"data":list(allcountries.values())})

def states(request):
    cid = request.GET['cid']
    allstates = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(allstates.values())})

def cities(request):
    sid = request.GET['sid']
    allcity= City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(allcity.values())})