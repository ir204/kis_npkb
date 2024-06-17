from django import forms

from departments.models import Sector


class CompetenceTableSortFilterForm(forms.Form):
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), required=False, label="Сектор")