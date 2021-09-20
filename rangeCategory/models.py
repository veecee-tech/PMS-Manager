from django.db import models
from django.utils import timezone

from authentication.models import User


# Create your models here.



class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ChargeChoices(models.TextChoices):
    PERCENTAGE = u'percentage', 'Percentage'
    QUANTITY = u'quantity', 'Quantity'


class Range(models.Model):
    # charge_type_choices = (('percentage', 'Percentage'), ('quantity', 'Quantity'))

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    charge_type = models.CharField(choices=ChargeChoices.choices, default=ChargeChoices.PERCENTAGE, max_length=50)
    charge_amount = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     # return self.in_category
