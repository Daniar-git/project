from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from project.user.models import User

