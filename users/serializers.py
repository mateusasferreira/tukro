from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location', 'birth_date', 'password']

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = User.objects.create_user(password=password, **validate_data)
        return user
