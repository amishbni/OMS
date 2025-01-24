from rest_framework import serializers

from core.serializers import BaseSerializer
from order.models import Product, Order, OrderItem


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = BaseSerializer.Meta.fields + ("id", "name", "price",)


class OrderItemSerializer(BaseSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = OrderItem
        fields = BaseSerializer.Meta.fields + ("id", "product", "product_id", "count",)


class OrderSerializer(BaseSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = BaseSerializer.Meta.fields + ("id", "user", "price", "items",)

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(
                order=order,
                product=item_data["product_id"],
                count=item_data["count"],
            )

        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["items"] = OrderItemSerializer(instance.items.all(), many=True).data
        return representation