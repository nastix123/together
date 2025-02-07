from rest_framework import serializers
from .models import User, Request, Response

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
        model = Request
        fields = '__all__'
        read_only_fields = ('author', 'created_at')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'
        read_only_fields = ('volunteer', 'created_at')