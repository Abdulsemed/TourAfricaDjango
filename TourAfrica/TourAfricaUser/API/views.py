from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from random import randint
from datetime import datetime, timedelta, timezone


from TourAfricaUser.API.serializers import(
    UserSerializer, 
    UserDetailSerializer,
    UserLoginSerializer,
    UserEmailSerializer,
    OTPSerializer,
    
)
from TourAfricaUser.common.emailsender import send_email

from TourAfricaUser.API.permissions import IsOwnerorReadOnly
from TourAfricaUser.models import (
    User, 
    OTP)
from TourAfricaUser.common.commonresponse import BaseResponse
from TourAfricaUser.common.otpgenerator import verify_OTP_Template, createOTP

# Create your views here.

# user views

class UserCreateAV(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        response = BaseResponse()
        if serializer.is_valid():
            serializer.save()
            otpvalue = createOTP()
            user = User.objects.get(email = serializer.data.get('email', ''))
            otp = OTP.objects.create(user=user,otp = otpvalue, expired_at = datetime.now(tz=timezone.utc) + timedelta(minutes=5))
            # otp.save()
            html_content = verify_OTP_Template(otpvalue)
            send_email("OTP Verification",[user.email],"" ,html_content)
            response = BaseResponse(status_code=201,success=True, message="User created successfully", data={'user':serializer.data})
        else:
            response = BaseResponse(status_code=400, success=False, message="Invalid user details", data=serializer.errors)    
            
        return Response(response.to_dict(), status= response.status_code)
    
    
class UserListAV(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    
    
class UserDetailAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerorReadOnly]
    
class UserLoginAV(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.data.get('email', ''))
            user_detail = UserDetailSerializer(user)
            tokens = RefreshToken.for_user(user=user)
            access_token = str(tokens.access_token)
            refresh_token = str(tokens)
            response = BaseResponse(
                status_code=200,data={"user":user_detail.data, "access_token":access_token, "refresh_token":refresh_token}
                , message="user logged in successfully", 
                success=True)
        else:
            response = BaseResponse(status_code=400, Error=serializer.errors, message="invalid credentials", success=False)
            
        return Response(response.to_dict(), status=response.status_code)
    
    
# otp views

class OTPVerifyAV(APIView):
    def post(self, request):
        try:
            serializer = OTPSerializer(data= request.data)
            response = BaseResponse()
            if serializer.is_valid():
                otp = serializer.validated_data.get('otp', '')
                user = User.objects.get(email=serializer.validated_data.get('email', ''))
                otp_obj = OTP.objects.get(user=user)
                
                if otp_obj.otp != otp:
                    response = BaseResponse(status_code=400, success=False, message="Invalid OTP or expired OTP")
                    
                elif  (datetime.now(timezone.utc) -  otp_obj.expired_at).total_seconds() > 0:
                    response = BaseResponse(status_code=400, success=False, message="OTP expired, sent a new OTP")
                    otpvalue = createOTP()
                    new_otp = OTP.objects.update(user=user,otp = otpvalue, expired_at = datetime.now(tz=timezone.utc) + timedelta(minutes=5))
                    new_otp.save()
                    html_content = verify_OTP_Template(otpvalue)
                    send_email("OTP Verification",[user.email],"" ,html_content)
                    
                else:
                    otp_obj.delete()
                    response = BaseResponse(status_code=200, success=True, message="OTP verified successfully")
                    
            else:
                response = BaseResponse(status_code=400, success=False, message="Invalid OTP details", data=serializer.errors)
        except User.DoesNotExist:
            response = BaseResponse(status_code=400, success=False, message="OTP verification failed")
        except OTP.DoesNotExist:
            response = BaseResponse(status_code=400, success=False, message="OTP verification failed")
            
        return Response(response.to_dict(), status=response.status_code)
    
class OTPCreateAV(APIView):
    def post(self, request):
        try:
            serializer = UserEmailSerializer(data= request.data)
            response = BaseResponse()
            if serializer.is_valid():
                user = User.objects.get(email=serializer.data.get('email', ""))
                otp_value = createOTP()
                otp = OTP.objects.get(user=user)
                OTP.objects.update(user=user, otp=otp_value, expired_at = datetime.now(tz=timezone.utc) + timedelta(minutes=5))
                html_content = verify_OTP_Template(otp_value)
                send_email("OTP Verification",[user.email],"",html_content)
                response = BaseResponse(status_code=200, success=True, message="OTP sent successfully")
            else:
                response = BaseResponse(status_code=400, success=False, message="Invalid user details", data=serializer.errors)
        except User.DoesNotExist:
            response = BaseResponse(status_code=400, success=False, message="User not found")
        except OTP.DoesNotExist:
            response = BaseResponse(status_code=400, success=False, message="Failed to send OTP")
        return Response(response.to_dict(), status=response.status_code)
        
        