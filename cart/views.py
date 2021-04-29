from django.db.models import Q
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

    def datatable_search(self, queryset):
        """
        :param queryset:
        :return: queryset by filtering search value
        """
        search_value = self.request.query_params.get('search')
        if search_value:
            if search_value.isdigit():
                return queryset.filter(
                    Q(order_num=int(search_value)) |
                    Q(total_item=int(search_value)) |
                    Q(total_price=int(search_value))
                )
            return queryset.filter(client_name__icontains=search_value)
        return queryset

    def datatable_filter(self, queryset):
        """
        :param queryset:
        :return: queryset order by order_value
        """
        order_value = self.request.query_params.get('order')
        if order_value:
            return queryset.order_by(order_value)
        return queryset
