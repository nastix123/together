from rest_framework import viewsets, permissions

from .models import RequestModel, ResponseModel, User
from .serializers import RequestSerializer, ResponseSerializer, UserLoginSerializer
from .permissions import IsNeedy, IsVolunteer

from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer

from rest_framework.authtoken.models import Token
from rest_framework.decorators import action


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


class UserRegistrationView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user_id": user.pk,
            "email": user.email,
            "user_type": user.user_type
        }, status=status.HTTP_200_OK)


class UserLogoutView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def logout(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)