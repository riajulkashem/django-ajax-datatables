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

    def test_all_list_of_orders(self):
        response = self.client.get(reverse('cart:order_list'))
        # Convert Order Dict Object Into JSON Dict
        data = json.loads(json.dumps(response.data))
        self.assertEqual(len(data['results']), 5)

    def test_limit_paginated(self):
        response = self.client.get(
            reverse('cart:order_list'),
            data={'limit': 2}
        )
        data = json.loads(json.dumps(response.data))
        self.assertEqual(len(data['results']), 2)

    def test_search(self):
        response = self.client.get(
            reverse('cart:order_list'),
            data={'search': 'Riajul'}
        )
        data = json.loads(
            json.dumps(response.data)
        )
        self.assertEqual(data['results'][0]['client_name'], 'Riajul')

    def test_list_order(self):
        response = self.client.get(
            reverse('cart:order_list'),
            data={'order': 'total_price'}
        )
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data['results'][0]['total_price'], 45340)
        first_row_price = data['results'][0]['total_price']
        second_row_price = data['results'][1]['total_price']
        self.assertTrue(
            first_row_price < second_row_price
        )
