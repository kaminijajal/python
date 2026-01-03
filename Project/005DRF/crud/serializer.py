from rest_framework import serializers
from crud.models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields='__all__'

    # def validate(self, attrs):
    #     errors = {}
    #     # print(attrs)
    #     if attrs.get('age') is not None and attrs['age']<18:
    #        errors['age'] = "Age must be above 18"

    #     if attrs.get('name') is not attrs['name'].isalpha():
    #         errors['name'] = "only characters allowed in name"
    #     if errors:
    #         raise serializers.ValidationError(errors)
    #     return attrs
    

    def validate(self, attrs):
        errors = {}

        # Age validation
        if attrs.get('age') is not None and attrs['age'] < 18:
            errors['age'] = "Age must be above 18"

        # Name validation
        if attrs.get('name') and not attrs['name'].isalpha():
            errors['name'] = "Only characters allowed in name"

        # If any errors exist, raise them together
        if errors:
            raise serializers.ValidationError(errors)

        return attrs