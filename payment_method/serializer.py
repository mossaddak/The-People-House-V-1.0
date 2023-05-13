from rest_framework import serializers
from .models import Charge

class ChargeSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    class Meta:
        model = Charge 
        fields = ('id', 'amount', 'created', 'stripe_charge_id', 'user')