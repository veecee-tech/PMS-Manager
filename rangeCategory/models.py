from django.db import models
# from authentication.models import User
# from django.contrib .auth.models import r
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL)
    category_name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.category_name
    