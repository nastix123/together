from django.contrib.auth.models import Group
from .models import Custom_User, RequestModel, ResponseModel
from django.core.exceptions import ValidationError

from rest_framework import serializers


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'
        read_only_fields = ('author', 'created_at')


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseModel
        fields = '__all__'


class RegistrationUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField()

    class Meta:
        model = Custom_User
        fields = ('phone', 'password', 're_password',)

    def validate(self, data):
        password = data.get('password')
        re_password = data.get('re_password')
        if password != re_password:
            raise ValidationError('Passwords do not match')
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ['phone', 'user_type', ]


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Custom_User
        fields = ['id', 'phone', 'user_type', ]
