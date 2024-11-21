import uuid
from django.db import models

from TourAfricaUser.models import User

# Create your models here.
    

class Transport(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, )
    type = models.CharField(max_length=50, )
    capacity = models.IntegerField()
    images = models.JSONField()
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Food(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, )
    type = models.CharField(max_length=50,choices=[("1", "breakfast"), ("2","brunch"),("3", "lunch"),("4","supper"),("5","dinner")])
    price = models.FloatField()
    description = models.TextField(max_length=1000, )
    people_count = models.PositiveIntegerField(default =1)
    images = models.JSONField()
    is_available = models.BooleanField(default=False)
    calorie_count = models.PositiveIntegerField()
    content = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Accomodation(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=100, )
    place_name = models.CharField(max_length=50, )
    price = models.FloatField()
    room_count = models.PositiveIntegerField(default= 1)
    images = models.JSONField()
    chekck_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=100, )
    city = models.CharField(max_length=100, )
    description = models.TextField(max_length=1000, )
    images = models.JSONField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    itinerary = models.ForeignKey(Itinerary, related_name="itenerary", default=None, on_delete=models.DO_NOTHING)
    accomodation = models.ForeignKey(Accomodation, related_name="accomadation", default=None, on_delete=models.DO_NOTHING)
    food = models.ForeignKey(Food, related_name="food", default=None, on_delete=models.DO_NOTHING)
    transport = models.ForeignKey(Transport, related_name="transport", default=None, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name="booked_user", default=None, on_delete=models.DO_NOTHING)
    pre_pay = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    arrival_address = models.TextField(default="Addis Ababa, Ethiopia")
    arrival_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # calculate the total price inside the serializer
    
class TourGuide(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, )
    
    user = models.ForeignKey(User, related_name="tour_guide_user", default=None, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    