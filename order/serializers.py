from core.serializers import BaseSerializer
from order.models import Product, Order, OrderItem


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = BaseSerializer.Meta.fields + ("id", "name", "price",)


class OrderItemSerializer(BaseSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = BaseSerializer.Meta.fields + ("id", "product", "order", "count",)


class OrderSerializer(BaseSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = BaseSerializer.Meta.fields + ("id", "user", "price", "items",)
