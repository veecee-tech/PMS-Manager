from django.contrib import admin
from .models import Category, Range
# Register your models here.

admin.site.register([Category, Range])