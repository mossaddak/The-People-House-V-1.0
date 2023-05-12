from rest_framework.serializers import ModelSerializer
from .models import (
    NewsLetter
)

class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ("__all__")
