from rest_framework.serializers import ModelSerializer
from .models import (
    NewsLetter,
    Invitation
)

class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ("__all__")

class InvitationSerializer(ModelSerializer):
    class Meta:
        model = Invitation
        fields = ("__all__")
