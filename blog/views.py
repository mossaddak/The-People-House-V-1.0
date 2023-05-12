from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import(
    Blog,
    Comment
)
from .serializer import(
    BlogSerializer,
    CommentSerializer
)
from datetime import datetime
from rest_framework import (
    permissions
)
from rest_framework.viewsets import (
    ModelViewSet
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticated
)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user



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
    

class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        
