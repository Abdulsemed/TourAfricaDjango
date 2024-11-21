from random import randint
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers
from datetime import datetime, timedelta

from TourAfricaUser.models import OTP, User

class UserSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(write_only=True, max_length=150)
    class Meta:
        model = User
        exclude = ["image"]
        extra_kwargs ={'password':{'write_only':True},}
        
    def validate(self, data):
        confirmPassword = data.get('confirmPassword')
        password = data.get('password')
        if password != confirmPassword:
            raise serializers.ValidationError("Passwords do not match")
        
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        
        return data
    
    
    def save(self):
        user = User.objects.create(
            full_name=self.validated_data['full_name'],
            email=self.validated_data['email'],
            password= make_password(self.validated_data['password']),
            type=self.validated_data['type'],
            image = None
        )
       
        user.save()
        
        return user
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password':{'write_only':True}}
        
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, data):
        email = data.get('email', "")
        password = data.get('password', "")
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email or password is incorrect")
        
        user = User.objects.get(email=email)
        if not check_password(password, user.password):
            raise serializers.ValidationError("Email or password is incorrect")
        
        if OTP.objects.filter(user=user).exists():
            raise serializers.ValidationError("user is not verified")
        
        return data
    
class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
        
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist")
        
        return email
    
# otp serializer

class OTPSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    class Meta:
        model = OTP
        fields = ['email', 'otp']
    
    def validate(self, data):
        email = data.get('email')
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist")
        
        return data