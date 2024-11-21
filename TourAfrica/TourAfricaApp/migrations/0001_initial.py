# Generated by Django 5.1.3 on 2024-11-20 07:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TourAfricaUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('place_name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('room_count', models.PositiveIntegerField(default=1)),
                ('images', models.JSONField()),
                ('chekck_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('1', 'breakfast'), ('2', 'brunch'), ('3', 'lunch'), ('4', 'supper'), ('5', 'dinner')], max_length=50)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=1000)),
                ('people_count', models.PositiveIntegerField(default=1)),
                ('images', models.JSONField()),
                ('is_available', models.BooleanField(default=False)),
                ('calorie_count', models.PositiveIntegerField()),
                ('content', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('images', models.JSONField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('images', models.JSONField()),
                ('is_available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourGuide',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tour_guide_user', to='TourAfricaUser.user')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pre_pay', models.BooleanField(default=False)),
                ('is_reserved', models.BooleanField(default=False)),
                ('arrival_address', models.TextField(default='Addis Ababa, Ethiopia')),
                ('arrival_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accomodation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accomadation', to='TourAfricaApp.accomodation')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='booked_user', to='TourAfricaUser.user')),
                ('food', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='food', to='TourAfricaApp.food')),
                ('itinerary', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='itenerary', to='TourAfricaApp.itinerary')),
                ('transport', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transport', to='TourAfricaApp.transport')),
            ],
        ),
    ]