from django.contrib import admin
from django.urls import path, include
from .views import (
    BlogView,
    CommentView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"comment", CommentView, basename="comment")

urlpatterns = [
    path("blogs/", BlogView.as_view())
]+router.urls
