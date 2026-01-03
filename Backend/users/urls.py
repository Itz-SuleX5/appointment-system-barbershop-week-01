from django.urls import path
from .views import CustomTokenObtainPairView, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
     path('register/', UserRegisterView.as_view(), name='register'),
     path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

