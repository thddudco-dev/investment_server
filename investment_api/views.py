from django.shortcuts import render
from rest_framework.response import Response
from .models import Investment_API
from rest_framework.views import APIView
from .serializers import Investment_APISerializer

# Create your views here.
class Invenstment_APIInfoAPI(APIView):
    def get(self, request):
        queryset = Investment_API.objects.all()
        print(queryset)
        serializer = Investment_APISerializer(queryset, many = True)
        return Response("serializer.data")