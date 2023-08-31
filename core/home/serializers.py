from rest_framework import serializers
from .models import *
import re

class StudentSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Student
        # fields = ['name','age']   #specific fields we want
        # exclude = ['id',]  # excluding id we get all data
        fields = '__all__'  # here we get all Data from model
        
    def validate(self, data):
        required_fields = ('name', 'age', 'father_name')
        #check any of these missing from the data
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise serializers.ValidationError(f"The following fields are required: {', '.join(missing_fields)}")
        
        name = data.get('name', '')
        if not re.match('^[a-zA-Z ]{1,20}$', name):
            raise serializers.ValidationError("Name can only contain alphabets, and must start with a capital or lowercase letter")
        
        age = data.get('age', None)
        if age is not None:
    
            if age <18:
                raise serializers.ValidationError("Age should not be less than 18")

        father_name = data.get('father_name', '')
        if not re.match('^[a-zA-Z ]{1,20}$', father_name):
            raise serializers.ValidationError("Father name can only contain alphabets, and must start with a capital or lowercase letter")

        return data
        