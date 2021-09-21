from django.db import models
from django.utils import timezone

from authentication.models import User


# Create your models here.


class RangeTypeChoices(models.TextChoices):
    customer_fee = u'customer fee for withdrawal', 'Customer Fee For Withdrawal'
    withdrawal_fee = u'pos fee for withdrawal', 'Pos Fee For Withdrawal'
    transfer_fee = u'pos fee for transfer', 'Pos Fee For Transfer'

class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    range_type = models.CharField(choices=RangeTypeChoices.choices, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name +" : " +self.range_type


class ChargeChoices(models.TextChoices):
    PERCENTAGE = u'percentage', 'Percentage'
    QUANTITY = u'quantity', 'Quantity'


class Range(models.Model):

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    charge_amount = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} : {} - {}".format(self.category, self.min_value, self.max_value) 

