from rest_framework import viewsets

from core.permissions import IsAuthenticatedOrCreate
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrCreate]
    queryset = User.objects.all()
    serializer_class = UserSerializer
