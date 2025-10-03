from django.urls import path
from myvegetable.views import *

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('blog-single',blogsingle,name='blog-single'),
    path('blog',blog,name='blog'),
    path('cart',cart,name='blog'),
    path('checkout',checkout,name='checkout'),
    path('contact',contact,name='contact'),
    path('product-single',productsingle,name='product-single'),
    path('shop',shop,name='shop'),
    path('wishlist',wishlist,name='wishlist')
]
