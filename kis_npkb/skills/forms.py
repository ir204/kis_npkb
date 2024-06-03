from django import forms

from departments.models import Department


class SkillSortFilterForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, label="Отдел")