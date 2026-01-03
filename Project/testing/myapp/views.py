from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse

import requests
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    return render(request,'index.html')


def payment(request):
    amt = request.GET.get("amt")

    if not amt:
        return JsonResponse({"error": "Amount not provided"}, status=400)

    amt = int(amt)

    client = razorpay.Client(auth=("rzp_test_RZXKBwmotI55aB", "SIufDu3mGeURc3zbcVJSo2fQ"))

    order = client.order.create({
        "amount": amt * 100,
        "currency": "INR",
        "receipt": "order001"
    })

    return JsonResponse(order)

