from rest_framework import serializers
from .models import programer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programer
        #fields= ('Fullname','nickname','age')
        fields= '__all__'