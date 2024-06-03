from django import forms
from departments.models import Department
from .const import CHOICES


def get_choices():
    choices = [(k,v) for k,v in CHOICES.items()]
    return choices


class EmployeeSortFilterForm(forms.Form):
    usertext = forms.CharField(required=False, widget=forms.TextInput, label="Поиск по фамилии")
    # search_by = forms.ChoiceField(choices=CHOICES, label="Поиск по", required=False)
    search_by = forms.ChoiceField(choices=get_choices(), label="Поиск по", required=False)
    fired = forms.BooleanField(required=False, label="Уволенные")
    # department = forms.ChoiceField(choices=Department.objects.all())

    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False)
    selected = forms.CharField(widget=forms.HiddenInput, required=False)
    selected_emp = forms.CharField(widget=forms.HiddenInput, required=False)
    is_skill = forms.BooleanField(widget=forms.HiddenInput, required=False)



