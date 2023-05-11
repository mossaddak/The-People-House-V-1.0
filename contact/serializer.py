from rest_framework.serializers import ModelSerializer
from .models import (
    Contact
)
from rest_framework import serializers


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ("__all__")
