from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['updated']


class Item(TimeStampedModel):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    order_num = models.IntegerField()
    client_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.client_name}"

    @property
    def total_item(self):
        return sum([item.quantity for item in self.items.all()])

    @property
    def total_price(self):
        return sum([item.items_price() for item in self.items.all()])


class OrderItem(TimeStampedModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        null=True
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'Item: {self.item.name} Quantity {self.quantity}'

    def items_price(self):
        return self.item.price * self.quantity
