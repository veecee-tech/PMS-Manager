from django.shortcuts import render
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# from .serializers import CategoryAPIViewSerializer, RangeAPIViewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rangeCategory.models import Category, Range
from rest_framework import permissions  
from .permissions import IsOwner
from rest_framework.response import Response

# Create your views here.
