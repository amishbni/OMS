from rest_framework import serializers

from core.models import BaseModel


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ("created_at", "updated_at",)
        read_only_fields = ("created_at", "updated_at",)
