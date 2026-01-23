from rest_framework import serializers
from myapp.models import *

class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"