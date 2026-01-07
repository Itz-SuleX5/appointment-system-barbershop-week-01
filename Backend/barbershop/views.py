import datetime
from django.shortcuts import render
from .models import Appointment, Category, Service, Combo
from rest_framework import viewsets
from .serializers import AppointmentSerializer, CategorySerializer, ServiceSerializer, ComboSerializer, BarberSerializer
from .permissions import IsAdminForUnsafeMethods
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from datetime import time, timedelta, datetime

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

class ValidateAppointmentView(APIView):
    def get(self, request):
        date_str = request.query_params.get('date')
        barber_id = request.query_params.get('barber')

        if not date_str:
            return Response({'error' : 'date parameter is required'}, status=400)
        
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD'}, status=404)
        
        start = time (9,0)
        end = time(14,0)
        slots=[]
        current = datetime.combine(date_obj, start)
        end_dt = datetime.combine(date_obj, end)
        while current <= end_dt:
            slots.append(current.time().strftime('%H:%M'))
            current += timedelta(minutes=30)

        appointments = Appointment.objects.filter(date=date_obj)
        if barber_id:
            appointments = appointments.filter(barber_id=barber_id)

        taken_times = set(a.time.strftime('%H:%M') for a in appointments)

        available_slots = [slot for slot in slots if slot not in taken_times]
        return Response({'available_slots': available_slots})