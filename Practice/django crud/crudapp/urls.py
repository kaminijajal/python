from django.urls import path
from crudapp.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name='reg'),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("update",update,name="update"),
    path("edit",edit,name="edit"),
    # path()
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)