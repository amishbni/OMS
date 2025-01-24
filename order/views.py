from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from order.models import Order, Product, OrderItem
from order.serializers import OrderSerializer, ProductSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
