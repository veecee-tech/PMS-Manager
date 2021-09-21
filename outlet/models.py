from django.db import models
from django.utils import timezone

from authentication.models import User


class Outlet(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=User)
    outlet_name = models.CharField(max_length=200, blank=False, null=False)
    outlet_address = models.TextField()
    outlet_officer = models.CharField(max_length=100, default="officer_name")
    customer_fee = models.CharField(max_length=200)
    transfer_fee = models.CharField(max_length=200)
    withdrawal_fee = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.outlet_name
