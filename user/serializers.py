from rest_framework import serializers

from core.serializers import BaseSerializer
from user.models import User


class UserSerializer(BaseSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = BaseSerializer.Meta.fields + ("id", "username", "email", "role", "password",)
