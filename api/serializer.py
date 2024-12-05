from rest_framework import serializers
from .models import programer, student

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programer
        #fields= ('Fullname','nickname','age')
        fields= '__all__'
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        #fields= ('Fullname','nickname','age')
        fields= '__all__'