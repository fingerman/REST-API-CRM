from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .serializers import SignUpSerializer, ProfileSerializer


UserModel = get_user_model()


class SignUp(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = UserModel.objects.all()
    serializer_class = SignUpSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser, )


