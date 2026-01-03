
from django.urls import path
from crudapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",index,name="index"),
    path('reg',reg,name='reg'),
    path('display',display,name='display'),
    path('delete',delete_student,name='delete'),
    path('edit',student_by_id,name='edit'),
    path('update',updatr_student,name='update'),
    

    path("userreg",user_reg,name="userreg"),
    path("userlogin",user_login,name="userlogin")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)