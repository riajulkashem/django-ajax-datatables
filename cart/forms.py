from django import forms
from django.forms import inlineformset_factory

from cart.models import OrderItem, Order


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm,
    fields=['item', 'quantity'], extra=1, can_delete=True
)
