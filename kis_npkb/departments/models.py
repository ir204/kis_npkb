from django.db import models

from general.model_mixins import NameMixin

# Create your models here.


class Department(NameMixin, models.Model):
    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class Sector(NameMixin, models.Model):
    objects = models.Manager()
    department = models.ForeignKey("Department", on_delete=models.CASCADE, verbose_name="Отдел")
    excel = models.FileField(verbose_name="Excel", blank=True, null=True)
    diagramm = models.ImageField(verbose_name="Диаграмма", blank=True, null=True)

    class Meta:
        verbose_name = "Сектор"
        verbose_name_plural = "Секторы"
