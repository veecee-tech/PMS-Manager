from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email','phone_number', 'full_name', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        # username = attrs.get('username', '')
        # phone_number = attrs.get('phone_number', '')
        # if not username.isalnum():
        #     raise serializers.ValidationError('the username should only contain alphanumeric character')
        
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    # username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled, Contact Admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            # 'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)


class RequestPasswordEmailRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        model =User
        fields = ['email']

    def validate(self, attrs):
            
            email = attrs['data'].get('email', '')

class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'token', 'uidb64']

        def validate(self, attrs):
            try:
                password= attrs.get('password')
                token = attrs.get('token')
                uidb64 = attrs.get('uidb64')

                id = urlsafe_base64_decode(force_str(uidb64))

                user =User.objects.get(id=id)

                if not PasswordResetTokenGenerator().check_token(user, token):
                    raise AuthenticationFailed('the reset link is invalid', 401)
                user.set_password(password)
                user.save()
                # return user
            
            except Exception as e:
                 raise AuthenticationFailed('the reset link is invalid', 401)
            return super().validate(attrs)
    
