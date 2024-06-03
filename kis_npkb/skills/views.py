from django.shortcuts import render
from django.views.generic import DetailView, ListView

from departments.models import Department
from .forms import SkillSortFilterForm
from .models import EmpSkill

# Create your views here.


class SkillListView(ListView):
    model = EmpSkill
    template_name = "skills/skill_list.html"

    def get_queryset(self):
        queryset = EmpSkill.objects.all()
        department = self.request.GET.get("department")
        if department:
            queryset = queryset.filter(sector__department_id=department)
        else:
            queryset = queryset.filter(sector__department_id=Department.objects.values_list("id", flat=True).first())
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = SkillSortFilterForm(self.request.GET)
        return context_data


# отдельное вью под график