from django.shortcuts import render
from .models import Appointment, Category, Service, Combo
from rest_framework import viewsets
from .serializers import AppointmentSerializer, CategorySerializer, ServiceSerializer, ComboSerializer, BarberSerializer
from .permissions import IsAdminForUnsafeMethods
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

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

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class BarberListView(APIView):
    def get(self, request):
        barbers = User.objects.filter(role='barber')
        serializer = BarberSerializer(barbers, many=True)
        return Response(serializer.data)