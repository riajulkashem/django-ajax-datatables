from django.views.generic import ListView
from cart.models import Order


class OrderListView(ListView):
    template_name = 'order_list.html'
    model = Order
