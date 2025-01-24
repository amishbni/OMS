from django.test import TestCase
from user.models import User
from order.models import Product, Order, OrderItem


class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Test Product", price=100.00)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100.00)

    def test_product_str(self):
        product = Product.objects.create(name="Test Product", price=100.00)
        self.assertEqual(str(product), "Test Product at 100.00")


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com")

    def test_create_order(self):
        order = Order.objects.create(user=self.user, price=200.00)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.price, 200.00)

    def test_order_str(self):
        order = Order.objects.create(user=self.user, price=200.00)
        self.assertEqual(str(order), f"{self.user}: 200.00")


class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com")
        self.product = Product.objects.create(name="Test Product", price=100.00)
        self.order = Order.objects.create(user=self.user, price=200.00)

    def test_create_order_item(self):
        order_item = OrderItem.objects.create(product=self.product, order=self.order, count=2)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.count, 2)

    def test_order_item_str(self):
        order_item = OrderItem.objects.create(product=self.product, order=self.order, count=2)
        self.assertEqual(str(order_item), f"{self.order}: 2 Test Product at 100.00")

    def test_save_order_item_increases_order_price(self):
        order_item = OrderItem.objects.create(product=self.product, order=self.order, count=2)
        self.order.refresh_from_db()
        self.assertEqual(self.order.price, 400.00)

    def test_update_order_item_changes_order_price(self):
        order_item = OrderItem.objects.create(product=self.product, order=self.order, count=2)
        self.order.refresh_from_db()
        self.assertEqual(self.order.price, 400.00)

        order_item.count = 3
        order_item.save()

        self.order.refresh_from_db()
        self.assertEqual(self.order.price, 500.00)

    def test_remove_order_item_decreases_order_price(self):
        order_item = OrderItem.objects.create(product=self.product, order=self.order, count=2)
        self.order.refresh_from_db()
        self.assertEqual(self.order.price, 400.00)

        order_item.delete()

        self.order.refresh_from_db()
        self.assertEqual(self.order.price, 200.00)
