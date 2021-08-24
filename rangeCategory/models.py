from django.db import models
from django.db.models.enums import Choices
from authentication.models import User
# from django.contrib .auth.models import r
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.category_name 


class ChargeChoices(models.TextChoices):
    PERCENTAGE = u'percentage', 'Percentage'
    QUANTITY = u'quantity', 'Quantity'
    

class Range(models.Model):
    # charge_type_choices = (('percentage', 'Percentage'), ('quantity', 'Quantity'))

    in_category = models.ForeignKey(to=Category, on_delete=models.CASCADE, default=Category, null=True)
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    charge_type = models.CharField(choices=ChargeChoices.choices,default=ChargeChoices.PERCENTAGE, max_length=50)
    charge_amount = models.IntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.in_category