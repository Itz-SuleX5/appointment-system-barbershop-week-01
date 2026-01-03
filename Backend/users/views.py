from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegisterSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_Classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer