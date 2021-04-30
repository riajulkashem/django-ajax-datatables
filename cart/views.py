from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView
from rest_framework.generics import ListAPIView

from cart.forms import OrderItemFormSet, OrderForm
from cart.models import Order, OrderItem
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


class OrderUpdate(UpdateView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderForm
    success_url = reverse_lazy('cart:home')

    def get_context_data(self, **kwargs):
        data = super(OrderUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = OrderItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = OrderItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['items']
        with transaction.atomic():
            self.object = self.get_object()
            if order_items.is_valid():
                order_items.instance = self.object
                order_items.save()
        return super(OrderUpdate, self).form_valid(form)
