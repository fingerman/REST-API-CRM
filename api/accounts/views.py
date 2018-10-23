from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import SignUpSerializer

UserModel = get_user_model()


class SignUp(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = UserModel.objects.all()
