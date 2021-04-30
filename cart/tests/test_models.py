from django.test import TestCase

from cart.models import Item


class ItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(
            name='Chocolate',
            unit='ps',
            price=24
        )

    def test_item_object_data(self):
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, 'Chocolate')
        self.assertEqual(item.unit, 'ps')
        self.assertEqual(item.price, 24)
