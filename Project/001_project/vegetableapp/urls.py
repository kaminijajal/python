from django.urls import path
from vegetableapp.views import *
from django.conf import settings
from django.conf.urls.static import static

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

    path("register",register,name="register"),
    path("login",user_login,name="login"),
    path("logout",user_logout,name="logout"),

    path("addtocart",add_to_cart,name="addtocart"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)