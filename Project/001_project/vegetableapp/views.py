from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog_details(request):
    return render(request,'blog-details.html')

def blog(request):
    return render(request,'blog.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def main(request):
    return render(request,'main.html')

def shope_details(request):
    return render(request,'shop-details.html')

def shop_grid(request):
    return render(request,'shop-grid.html')

def shopping_cart(request):
    return render(request,'shoping-cart.html')
