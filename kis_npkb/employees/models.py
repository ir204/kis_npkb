from django.db import models
from django.urls import reverse

# Create your models here.


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(fired=False).order_by("surname")


class Employee(models.Model):
    objects = models.Manager()
    sorted = EmployeeManager()
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Имя")
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    post = models.CharField(max_length=150, blank=False, null=False, verbose_name="Должность")
    phone = models.PositiveIntegerField(blank=True, null=True, verbose_name="Телефон")
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True)
    fired = models.BooleanField(blank=False, null=False, default=False, verbose_name="Уволен")
    sector = models.ForeignKey("departments.Sector", on_delete=models.CASCADE, verbose_name="Сектор")

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={"pk": self.id})
