from project.common.models import Base
from project.user.models import User
from .constants import StatusType

from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(Base):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    todo_status = models.PositiveIntegerField(
        choices=StatusType.choices,
        default=StatusType.NOT_FINISHED,
        verbose_name=_('Todo status')
    )

    class Meta:
        verbose_name_plural = _("Todo")
