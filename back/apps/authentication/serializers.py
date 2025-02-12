from rest_framework import serializers
from .models import User, RequestModel, ResponseModel
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if not any([data.get('username'), data.get('email'), data.get('phone')]):
            raise serializers.ValidationError("At least one of username, email or phone is required.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'
        read_only_fields = ('author', 'created_at')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'
        read_only_fields = ('volunteer', 'created_at')


class UserLoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        login = data.get('login')
        password = data.get('password')

        if not login or not password:
            raise serializers.ValidationError("Both login and password are required.")

        user = authenticate(
            request=self.context.get('request'),
            username=login,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        data['user'] = user
        return data

    def create(self, validated_data):
        # Method required for DRF, but not used
        pass