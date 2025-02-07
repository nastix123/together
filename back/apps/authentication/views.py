from rest_framework import viewsets, permissions

from .models import RequestModel, ResponseModel
from .serializers import RequestSerializer, ResponseSerializer, UserLoginSerializer
from .permissions import IsNeedy, IsVolunteer
from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsNeedy]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = ResponseModel.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.IsAuthenticated, IsVolunteer]

    def perform_create(self, serializer):
        serializer.save(volunteer=self.request.user)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            login(request, user)  # Log the user in
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
