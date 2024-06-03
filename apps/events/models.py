from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.common.utils import get_default_event_date


class Event(BaseModel):
    title = models.CharField(_("Title"), db_index=True, max_length=100)
    description = models.TextField(_("Description"), max_length=1000)
    date = models.DateTimeField(_("Date"), default=get_default_event_date)
    organizer = models.ForeignKey(
        "users.User",
        verbose_name=_("User"),
        related_name="events",
        related_query_name="events",
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ("-created", "title")
        db_table = "event"
