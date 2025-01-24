from rest_framework import serializers

from core.serializers import BaseSerializer
from user.models import User


class UserSerializer(BaseSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = BaseSerializer.Meta.fields + ("id", "username", "email", "role", "password",)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
