from django.db import models
from authentication.models import User 
from django.utils import timezone



class CreateOutlet(models.Model):
    outlet_name = models.CharField(max_length=200, blank=False, null=True)
    outlet_address = models.TextField()
    outlet_officer = models.CharField(max_length=100, default="officer_name")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.outlet_name

        