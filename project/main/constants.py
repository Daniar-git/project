from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class StatusType(IntegerChoices):
    NOT_FINISHED = 0, _('NOT_FINISHED')
    DONE = 1, _('DONE')