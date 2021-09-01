from os import access
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, phone_number=None,full_name=None):

        # if username is None:
        #     TypeError("users Should Have a username")
        if email is None:
            TypeError("users Should Have an email")
        
        user = self.model(phone_number=phone_number, full_name=full_name, email=self.normalize_email(email))

        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
    
        if password is None:
            TypeError("password should not be none")

        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    # username = models.CharField(max_length=200, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone_number = PhoneNumberField(unique = True, null = True, blank = True)
    full_name = models.CharField(max_length=255, null=True,blank = True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # defining attribut to login

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    # manage update of type uuser 
      #instantiate the manager class
    objects = UserManager()
    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        # token =
        return {
            # 'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

