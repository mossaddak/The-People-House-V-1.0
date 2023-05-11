from django.contrib import admin
from django.urls import path, include
from .views import(
    ContactView
)

urlpatterns = [
    path('contact/', ContactView.as_view())
]
