from rest_framework import serializers
from .models import Investment_API

class Investment_APISerializer(serializers.ModelSerializer):
    class Meta:
        model =  Investment_API
        fields = '__all__'