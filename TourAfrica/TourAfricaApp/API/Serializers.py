from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from bcrypt import _bcrypt
from TourAfricaApp.models import (
    User,
    OTP)


    
    
# otp serializers

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = "__all__"
    
        