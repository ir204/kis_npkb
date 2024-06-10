from django import forms

from departments.models import Department, Sector


class CompetenceSortFilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, label="Отдел")


class CompetenceTableSortFilterForm(forms.Form):
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False, label="Сектор")