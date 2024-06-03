from django.db import models


class NameMixin(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="", verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
