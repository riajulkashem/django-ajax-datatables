from django.urls import path

from cart.views import Home, OrderListAPIView, OrderUpdate

app_name = 'cart'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('order-list/', OrderListAPIView.as_view(), name='order_list'),
    path(
        'order/<int:pk>/details/',
        OrderUpdate.as_view(),
        name='order_details'
    ),
]
