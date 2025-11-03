from django.shortcuts import render,HttpResponse
import razorpay

# Create your views here.
def index(request):
    return render(request,'index.html')

def payment(request):
    
    client = razorpay.Client(auth=("rzp_test_RZXKBwmotI55aB", "SIufDu3mGeURc3zbcVJSo2fQ"))

    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
    #  Amount is in currency subunits. Default currency is INR. 
    # Hence, 50000 refers to 50000 paise
    return HttpResponse(payment)