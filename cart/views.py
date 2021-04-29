from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from cart.models import Order
from cart.serializers import OrderSerializer


class Home(ListView):
    template_name = 'order_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

