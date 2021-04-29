from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, ButtonHolder, Submit, HTML
from django import forms
from django.forms import inlineformset_factory

from cart.custom_layout_object import Formset
from cart.models import OrderItem, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client_name']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('client_name'),
                Fieldset(
                    'Order Item Details',
                    Formset('items')
                ),
                HTML("<br>"),
                ButtonHolder(
                    Submit(
                        css_class="btn btn-success",
                        value='Update Order Detail',
                        name='submit'
                    ),
                    css_class='float-right',
                ),
            )
        )


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm,
    extra=0, can_delete=True
)
