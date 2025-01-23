from core.models import BaseModel
from django.db import models


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} at {self.price}"


class Order(BaseModel):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    count = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.order.price += (self.count * self.product.price)
            self.order.save(update_fields=["price"])
        else:
            order_item: OrderItem = OrderItem.objects.get(pk=self.pk)
            if order_item.count != self.count:
                changed_count: int = self.count - order_item.count
                self.order.price += (changed_count * self.product.price)
                self.order.save(update_fields=["price"])
        super().save(*args, **kwargs)

