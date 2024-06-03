from django import forms

from departments.models import Department


class CompetenceSortFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].required = False

        class Meta:
            model = Department
            fields = ["department", ]
            labels = {"department": "Отдел"}