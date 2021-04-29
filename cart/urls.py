from django.urls import path

from cart.views import OrderListView

app_name = 'cart'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
]
