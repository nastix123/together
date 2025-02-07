from rest_framework import viewsets, permissions

from .models import RequestModel, ResponseModel
from .serializers import RequestSerializer, ResponseSerializer
from .permissions import IsNeedy, IsVolunteer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
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