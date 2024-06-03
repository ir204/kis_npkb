from django.db import models

from general.model_mixins import NameMixin

# Create your models here.


class Skill(NameMixin, models.Model):
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class EmpSkill(models.Model):
    objects = models.Manager()
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE, verbose_name="Сотрудник", blank=True, null=True)
    skill = models.ForeignKey("Skill", on_delete=models.CASCADE, verbose_name="Навык")
    skill_level = models.PositiveIntegerField(verbose_name="Уровень владения")
    sector = models.ForeignKey("departments.Sector", on_delete=models.CASCADE, verbose_name="Сектор")

