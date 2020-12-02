from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from gde.models import *

User = get_user_model()

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    dispatcher= models.ForeignKey(Dispatcher, on_delete= models.PROTECT)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("price") * F("quantity"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
    def get_absolute_url(self):
        return reverse('detail_order', kwargs={'pk':self.id})


class OrderLine(models.Model):
    product = models.CharField(max_length= 20000)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places= 2, max_digits= 18, blank= False)

    def __str__(self):
        return f'{self.quantity} of {self.product}'

    class Meta:
        ordering= ['id']
