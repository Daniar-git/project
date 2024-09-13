from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse
from django.contrib.auth import authenticate

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer, LoginSerializer
from rest_framework import serializers, exceptions
from dj_rest_auth.models import TokenModel

from .models import User


class UserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)
        super(UserSerializer, self).__init__(*args, **kwargs)
        if self.context and 'view' in self.context and self.context['view'].__class__.__name__ == 'UsersView':
            exclude_fields = ['file']
        if exclude_fields:
            for field_name in exclude_fields:
                self.fields.pop(field_name)


    class Meta:
        fields = ('id', 'last_login', 'first_name', 'last_name', 'email', 'date_joined', 'birthdate',
                  'gender', 'file', 'phone', 'activated_date', 'birthplace', 'address', 'username')
        model = User


class UserRegistrationSerializer(RegisterSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email', None)


class UserDetailsSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField('is_key', read_only=True)
    user = serializers.SerializerMethodField('is_user', read_only=True)

    def is_key(self, obj):
        token = TokenModel.objects.filter(user=obj).first()
        if not token:
            token = TokenModel.objects.create(user=obj)
        return str(token)

    def is_user(self, obj):
        serializers = UserSerializer(obj)
        return serializers.data

    class Meta:
        fields = ('user', 'key')
        model = User


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = '__all__'


class ResetPasswordSerializer(PasswordResetSerializer):

    def get_email_options(self):
        return {
            'html_email_template_name': 'email/reset_password.html'
        }

    def validate(self, attrs):
        if not Site.objects.filter(pk=settings.SITE_ID_FRONTEND).exists():
            raise serializers.ValidationError(_('System error contact support please'))
        return attrs

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'request': request
        }
        opts.update(self.get_email_options())
        site = Site.objects.get(pk=settings.SITE_ID_FRONTEND)
        self.reset_form.save(**opts, domain_override=urlparse(request.META.get('HTTP_REFERER', site.domain)).netloc)
