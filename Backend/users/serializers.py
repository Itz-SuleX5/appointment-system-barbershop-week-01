from rest_framework import serializers
from .models import User
import uuid

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'role')
        extra_kwargs = {'username': {'read_only': True}}

    def create(self, validated_data):
        if not validated_data.get('username'):
            validated_data['username'] = uuid.uuid4().hex[:12]
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'client')
        )
        return user