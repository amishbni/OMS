from django.urls import path, include

from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet, ProductViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r"orders/items", OrderItemViewSet, basename="order-item")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"products", ProductViewSet, basename="product")

app_name = "orders"
urlpatterns = [
    path("", include(router.urls)),
]
