from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# from TourAfricaApp.API.Serializers import ()
from TourAfricaUser.API.permissions import IsOwnerorReadOnly

from TourAfricaApp.common.commonresponse import BaseResponse

# Create your views here.
