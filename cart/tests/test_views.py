import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


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
    client = APIClient()

    def test_url_exist_at_desired_location(self):
        response = self.client.get('/order-list/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cart:order_list'))
        self.assertEqual(response.status_code, 200)
