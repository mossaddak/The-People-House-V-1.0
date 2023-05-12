from django.contrib import admin
from django.urls import path, include
from .views import(
    NewsLetterView
)

urlpatterns = [
    path('newsletter/', NewsLetterView.as_view())
]
