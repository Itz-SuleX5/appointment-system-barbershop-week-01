from django.shortcuts import render
from .models import Category, Service, Combo
from rest_framework import viewsets
from .serializers import CategorySerializer, ServiceSerializer, ComboSerializer
from .permissions import IsAdminForUnsafeMethods

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminForUnsafeMethods]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminForUnsafeMethods]

class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    permission_classes = [IsAdminForUnsafeMethods]
