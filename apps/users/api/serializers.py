from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from apps.users.models import User


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {"bad_token": ("El Token ha expirado o es inválido")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, *args, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user

        def validate_password(self, value):
            if len(value) < 8:
                raise serializers.ValidationError(
                    "La contraseña debe tener al menos 8 caracteres"
                )
            return value


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "username"

        def to_representation(self, instance):
            return {
                "username": instance["username"],
            }


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password_confirm = serializers.CharField(
        max_length=128, min_length=8, write_only=True
    )

    def validate(self, data):
        if len(data["password"]) < 8 or len(data["password_confirm"]) < 8:
            raise serializers.ValidationError(
                {"La contraseña debe tener por lo menos 8 caracteres."}
            )
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError(
                {"password_confirm": "Ambas contraseñas deben ser iguales"}
            )
        return data
