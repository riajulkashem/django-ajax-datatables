from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):

    def test_template(self):
        response = self.client.get(reverse('cart:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_list.html')

