from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse

import requests
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')


# def payment(request):

#     amt = int(request.GET['amt'])
#     client = razorpay.Client(auth=("rzp_test_R8LF6p6eS7swQn", "WsLBNmXfF7C4e9T4vWgZaLeN"))

#     data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
#     payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    
#     return JsonResponse(payment)
def payment(request):
    # Static amount in INR
    amt = 500  # ₹500
    client = razorpay.Client(auth=("rzp_test_RZXKBwmotI55aB", "YOUR_SECRET_KEY"))

    data = {
        "amount": amt * 100,  # Razorpay expects amount in paise
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    try:
        order = client.order.create(data=data)
        return JsonResponse(order)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def send_email(request):

    emailto =request.GET['email-to']
    subject = request.GET['subject']
    message = request.GET['message']
    context = {}

    try:
        send_mail(subject,message,settings.EMAIL_HOST_USER,[emailto])
        context['result']  = 'Email sent successfully'
    except Exception as e:
        context['result'] = f'Error sending email: {e}'
        print(context)
    
    # return HttpResponse(context['result'])
    return render(request,'index.html',context)




