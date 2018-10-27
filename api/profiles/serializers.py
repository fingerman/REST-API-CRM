from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

UserModel = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(UserModel.objects.all())]
    )
    password = serializers.CharField(
        min_length=4,
        write_only=True
    )

    def create(self, validated_data):
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        data = {f: validated_data.get(f) for f in fields}
        return UserModel.objects.create_user(**data)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(UserModel.objects.all())]
    )

    class Meta:
        model = UserModel
        fields = 'id username email first_name last_name'.split()

'''
- add a field to the serilzer - hidden- owner
owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
- in the view add custom permisson
'''