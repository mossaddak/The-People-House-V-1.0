from django.contrib import admin
from django.urls import path, include
from .views import(
    NewsLetterView,
    ElectionStartView,
    InvitationView
)

urlpatterns = [
    path('newsletter/', NewsLetterView.as_view()),
    path('election-start/', ElectionStartView.as_view()),
    path('invitation/', InvitationView.as_view()),
]
