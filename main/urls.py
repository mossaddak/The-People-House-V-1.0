from django.contrib import admin
from django.urls import path, include
from .views import(
    NewsLetterView,
    ElectionStartView
)

urlpatterns = [
    path('newsletter/', NewsLetterView.as_view()),
    path('election-start/', ElectionStartView.as_view()) 
]
