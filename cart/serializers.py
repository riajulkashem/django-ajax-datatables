from rest_framework import serializers

from cart.models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_item = serializers.ReadOnlyField()
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'order_num', 'client_name', 'total_item', 'total_price']
