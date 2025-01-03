from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class AbsModel(models.Model):
    date_creation = models.DateTimeField(
        verbose_name=_("Date created"), blank=True, default=now, editable=False
    )
    date_updated = models.DateTimeField(verbose_name=_("Date updated"), auto_now=True)

    class Meta:
        abstract = True

    def update(self, **kwargs):  # noqa ANN201
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
