from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import(
    User
)
#serializer
from .serializer import(
    UserSerializer,
    VeriFyAccountSerializer,
    LoginSerializer
)
#otp verification
from .otp_send import send_otp_via_email
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework import (
    permissions
)
from rest_framework import parsers
from django.http import HttpResponse
from .payment import (
    subscription
)


#stripe connection
def stripe_connection(amount, token):
    amount = int(amount)
    user = User.objects.all().last()
    #subscription(amount, user, token)
    user.token = token
    user.subscription_fee = amount
    user.save()


# Create your views here.
class SingUp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
            if serializer.is_valid():

                #subscription
                subscription_type = request.data.get('subscription_type')

                if subscription_type == "Liberty plan":
                    serializer.save()

                elif subscription_type == "Patriot plan":
                    token = request.data.get('token')
                    subscription_type = "Patriot plan"
                    serializer.save()
                    amount = 1
                    stripe_connection(amount, token)

                elif subscription_type == "Eagle plan":
                    token = request.data.get('token')
                    serializer.save()
                    amount = 8
                    stripe_connection(amount, token)
                
                elif subscription_type == "Stars and Stripes plan":
                    token = request.data.get('token')
                    serializer.save()
                    amount = 15
                    stripe_connection(amount, token)

                elif subscription_type == "Founding Fathers plan":
                    token = request.data.get('token')
                    serializer.save()
                    amount = 20
                    stripe_connection(amount, token)

                
                user = User.objects.all().last()
                refresh = RefreshToken.for_user(user)
                serializer = UserSerializer(user).data
                return Response(
                    {   
                        'message':"Your account is successfully created",
                        'data':serializer,
                        'refresh_token': str(refresh),
                        'access_token':str(refresh.access_token)
                    },status = status.HTTP_201_CREATED
                )
        
        except Exception as e:
            print(e)
            return Response(
                    {
                        'message':"something Went Wrong",
                        'message':serializer.errors,
                    },status = status.HTTP_400_BAD_REQUEST  
                )
        
class VerifyOTPview(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VeriFyAccountSerializer(data=data)
            if serializer.is_valid():
                otp = serializer.data['otp']
                user = User.objects.filter(otp=otp)
                if not user.exists():
                    return Response(
                        {
                            'message':"Invalid OTP",
                            'error':"User not found"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                if not user[0].otp == otp:
                    return Response(
                        {
                            'message':"Please give here correct OTP",
                            'error':"Wront OTP"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                user = user[0]
                if user.is_verified == False:
                    user.is_verified = True
                    user.otp=""
                    user.save()
                    #print("OTPemail=====================================",user[0].verified)
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            'message':"Your account is verified now.",
                            'refresh_token': str(refresh),
                            'access_token':str(refresh.access_token)
                        },status = status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {
                            'message':"Your already verified your account"
                        },status = status.HTTP_201_CREATED
                    )

            
        except Exception as e:
            print("Error=======================================", e)

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'data':{},
                        'message':'something Went Wrong'
                    },status = status.HTTP_400_BAD_REQUEST
                )
            response = serializer.get_jwt_token(serializer.data)
            return Response(response,status = status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {
                    'data':{},
                    'message':"something Went Wrong"
                },status = status.HTTP_400_BAD_REQUEST
            )
        
#profile ================================================================>
class ProfileView(APIView): 
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        users = User.objects.all()
        user = request.user
        serializer = UserSerializer(user)
        response = Response(serializer.data)
        return response

    def patch(self, request):
        try:
            userid = request.user.id
            user = User.objects.get(pk=userid)
            data = request.data
            serializer = UserSerializer(user, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                response = Response(
                    {
                        'user': serializer.data,
                        'message': "Your profile has been updated"
                    },
                    status=status.HTTP_200_OK
                )
                return response
            else:
                response = Response(
                    {
                        'user': serializer.errors,
                        'message': "Your profile could not be updated"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
                return response

        except IntegrityError:
            response = Response(
                {
                    'user': None,
                    'message': "A user with that username already exists"
                },
                status=status.HTTP_409_CONFLICT
            )
            return response
        
        except Exception as e:
            print(e)
            response = Response(
                {
                    'user': None,
                    'message': "An error occurred while updating your profile"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            return response

class VerifiCationOtpSentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user
        email = request.user.email
        print("USER email==================================================>", email)
        if user.is_verified == False:
            user.otp=""
            user.save()
            send_otp_via_email(email)

            return Response(
                {
                    'message':"Check your mail, OTP is sent."
                },status = status.HTTP_200_OK
            
            )
        else:
            return Response(
                {
                    'message':"Your account is already verified."
                },status = status.HTTP_200_OK
            
            )