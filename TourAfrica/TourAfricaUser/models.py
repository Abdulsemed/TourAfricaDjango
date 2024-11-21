import uuid
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50, )
    email = models.EmailField(max_length=100, )
    password = models.CharField(max_length = 150, )
    type = models.CharField(max_length=50,choices=[("1","user"), ("2","admin"),("3","tour_guide")])
    image = models.TextField(max_length=150, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OTP(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    otp = models.CharField(max_length=6, )
    user = models.OneToOneField(User, related_name="otp_user", on_delete=models.CASCADE)
    expired_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)