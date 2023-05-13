from rest_framework.serializers import ModelSerializer
from .models import (
    User
)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status




def auto_user(set_email):
    provider = set_email.split("@")[1]
    usernames = {
        "gmail.com": "",
        "yahoo.com": "2",
        "hotmail.com": "3",
        "aol.com": "4",
        "outlook.com": "5",
        "icloud.com": "6",
        "protonmail.com": "7",
        "zoho.com": "8",
        "mail.com": "9",
        "gmx.com": "10",
    }

    # Generate the unique username based on the email provider
    if provider in usernames:
        username = set_email.split("@")[0] + usernames[provider]
    else:
        username = set_email.split("@")[0]

    return username


class UserSerializer(ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        is_superuser = serializers.BooleanField(read_only=True)
        is_verified = serializers.BooleanField(read_only=True)
        is_verified = serializers.BooleanField(read_only=True)
        fields = [
            'id',
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "birth_date",
            "phone",
            "state",
            "city",
            "country",
            "political_affiliation",
            "num_of_national_election_voted",
            "num_of_state_election_voted",

            
            "is_superuser",
            "is_verified",
            

            "is_subscribed",
            "subscription_type",
            "subscription_fee", #new
            "token"
        ]


        extra_kwargs = {
           "password": {"write_only":True, "style":{"input_type": "password"}},
           "is_superuser": {"read_only": True}, 
        }


    def get_username(self, obj):
        return obj.username

    def validate(self, data):
        request = self.context.get('request')
        current_user_id = request.user.id if request and request.user else None
        if User.objects.filter(email = data['email']).exclude(id=current_user_id).exists():
             raise serializers.ValidationError("email already exist")
        return data

    def create(self, validate_data):
        email = validate_data["email"]
        username = auto_user(email)
        user = User.objects.create(
            username=username,
            first_name=validate_data["first_name"],
            last_name=validate_data["last_name"],
            password=validate_data["password"],
            subscription_type=validate_data["subscription_type"],
            email=email
        )
        user.set_password(validate_data["password"])
        user.save()
        return validate_data
    
class VeriFyAccountSerializer(serializers.Serializer):
    otp = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Account not found")
        user = User.objects.filter(email=email)[0]
        if not authenticate(email=email, password=data['password']):
            raise serializers.ValidationError("Invalid credentials")
        return data

    def get_jwt_token(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        refresh = RefreshToken.for_user(user)
        serialized_user = UserSerializer(user).data
        return {
            'message': 'Login success',
            'data': serialized_user,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token)
        }