from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import(
    ContactSerializer
)

# Create your views here.
class ContactView(APIView):
    def post(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
        else:
            serializer.save()
            return Response(
                {
                    'data':serializer.data,
                    'message':"Thank you for contact us."
                }
            )