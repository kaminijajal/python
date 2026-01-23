from rest_framework import serializers
from myapp.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'

