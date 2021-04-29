from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from rest_framework.generics import ListAPIView

from cart.models import Order
from cart.serializers import OrderSerializer


class Home(View):
    template_name = 'order_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # ordering_fields = ('order_num', 'client_name', 'total_item', 'total_price')

    def datatable_search(self, queryset):
        """
        :param queryset:
        :return: queryset by filtering search value
        """
        search_value = self.request.query_params.get('search')
        if search_value:
            if search_value.isdigit():
                # Model Object Cant Filter or Order By Model Property
                return [q for q in queryset if int(search_value) in [q.order_num, q.total_item, q.total_price]]
            return queryset.filter(client_name__icontains=search_value)
        return queryset

    def datatable_filter(self, queryset):
        """
        :param queryset:
        :return: queryset order by order_value
        """
        order_value = self.request.query_params.get('order')
        if order_value:
            # Model Object Cant Filter or Order By Model Property
            return sorted(queryset, key=lambda row: getattr(row, order_value))
        return queryset

    def get_queryset(self):
        queryset = super(OrderListAPIView, self).get_queryset()
        searched_queryset = self.datatable_search(queryset)
        return self.datatable_filter(searched_queryset)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
