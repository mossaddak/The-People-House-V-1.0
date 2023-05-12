from rest_framework.serializers import ModelSerializer
from .models import (
    NewsLetter,
    ElectionStart
)

class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ("__all__")


class ElectionStartSerializer(ModelSerializer):
    class Meta:
        model = ElectionStart
        fields = ("__all__")
