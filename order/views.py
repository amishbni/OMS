from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import User
from order.models import Order, Product, OrderItem
from order.serializers import OrderSerializer, ProductSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user: User = self.request.user
        if user.is_admin:
            return Order.objects.all()
        return Order.objects.filter(user=user)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
