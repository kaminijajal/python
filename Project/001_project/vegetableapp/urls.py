from django.urls import path
from vegetableapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('blogdetails',blog_details,name='blog-details'),
    path('blog',blog,name='blog'),
    path('checkout',checkout,name='checkout'),
    path('contact',contact,name='contact'),
    path('main',main,name='main'),
    path('shopdetails',shope_details,name='shop-details'),
    path('shopgrid',shop_grid,name='shop-grid'),
    path('shopingcart',shopping_cart,name='shoping-cart'),
]
