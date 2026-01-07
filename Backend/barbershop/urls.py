from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, BarberListView, CategoryViewSet, ServiceViewSet, ComboViewSet, ValidateAppointmentView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'combos', ComboViewSet)
router.register(r'appointments', AppointmentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('barbers/', BarberListView.as_view(), name='barber-list'),
    path('validate-appointment/', ValidateAppointmentView.as_view(), name='validate-appointment'),
]
