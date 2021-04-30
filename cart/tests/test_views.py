from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class TestHomeView(TestCase):

    def test_template(self):
        response = self.client.get(reverse('cart:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')

    def test_url_exist_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class TestOrderListApiView(APITestCase):
    fixtures = ['item.json', 'order.json', 'order_item.json']

    def test_url_exist_at_desired_location(self):
        response = self.client.get('/')
        print(response.data)
        self.assertEqual(response.status_code, 200)
