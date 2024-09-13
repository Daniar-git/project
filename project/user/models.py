from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from uuid import uuid4

from project.common.models import Base


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'tests/{}/{}.{}'.format(instance.pk, uuid4(), ext)


class User(AbstractUser):
    GENDER = [
        ('male', _('Male')),
        ('female', _('Female')),
    ]
    birthdate = models.DateTimeField(null=True, blank=True, verbose_name=_('Birthdate'))
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
        verbose_name=_('Gender'),
        default='male',
    )
    file = models.ImageField(upload_to='avatar', null=True, blank=True, verbose_name=_('Avatar'))
    phone = models.CharField(max_length=30, blank=True, verbose_name=_('Phone number'))
    activated_date = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name=_('Activated date'))
    birthplace = models.CharField(max_length=100, blank=True, verbose_name=_('Birthplace'))
    address = models.CharField(max_length=200, blank=True, verbose_name=_('Address'))

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

