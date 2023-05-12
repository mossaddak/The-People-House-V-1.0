from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import(
    Blog
)
from .serializer import(
    BlogSerializer
)
from datetime import datetime


# Create your views here.

class BlogView(APIView):

    def get(self, request):
        queryset = Blog.objects.all()
        serializer = BlogSerializer(data=queryset, many=True)
        serializer.is_valid()
        response = {
            "data": serializer.data,
            "message": "Data successfully fetched"
        }
        return Response(response)
        
