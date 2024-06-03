from django.db import models

from general.model_mixins import NameMixin


# Create your models here.


class Competence(NameMixin, models.Model):
    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"


class EmpCompetence(models.Model):
    objects = models.Manager()
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, verbose_name="Сотрудник", blank=True, null=True)
    competence = models.ForeignKey("Competence", on_delete=models.CASCADE, verbose_name="Компетенция")
    competence_level = models.PositiveIntegerField(verbose_name="Уровень владения")
    sector = models.ForeignKey("departments.Sector", on_delete=models.CASCADE, verbose_name="Сектор")





