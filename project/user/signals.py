from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from project.user.models import User, Blog


@receiver(post_save, sender=User)
def create_ChannelToken(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(user=instance, name="first")
        instance.first_name = "Daniyar"
        instance.save()