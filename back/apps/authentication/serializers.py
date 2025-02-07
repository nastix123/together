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
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if not data.get('username') and not data.get('email'):
            raise serializers.ValidationError("Either username or email is required.")
        if not data.get('password'):
            raise serializers.ValidationError("Password is required.")
        return data

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")
        return user