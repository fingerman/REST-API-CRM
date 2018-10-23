from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(validators=[UniqueValidator(UserModel.objects.all())])
    password = serializers.CharField(
        min_length=6,
        write_only=True
    )

    # help function not to save users directly, but to pass validation in order to create password,... etc.
    def create(self, validated_data):
        fields = ['username', 'email', 'password']
        data = {f: validated_data.get(f) for f in fields}
        
        return UserModel.objects.create_user(**data)

    class Meta:
        model = UserModel
        fields = 'id username email first_name last_name password'.split()
