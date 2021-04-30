from django.test import TestCase

from cart.models import Item, OrderItem, Order


class OrderItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        order = Order.objects.create(
            order_num=1,
            client_name='Riajul Kashem'
        )
        item = Item.objects.create(
            name='Chocolate',
            unit='ps',
            price=24
        )
        OrderItem.objects.create(
            order=order,
            item=item,
            quantity=32
        )

    def test_item_data(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, 'Chocolate')
        self.assertEqual(item.unit, 'ps')
        self.assertEqual(item.price, 24)

    def test_order_item_data(self):
        order_item = OrderItem.objects.get(id=1)
        self.assertEqual(order_item.item_id, 1)
        self.assertEqual(order_item.quantity, 32)
        self.assertEqual(order_item.items_price(), 768)

    def test_order_data(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.order_num, 1)
        self.assertEqual(order.client_name, 'Riajul Kashem')
        self.assertEqual(order.total_item, 32)
        self.assertEqual(order.total_price, 768)
