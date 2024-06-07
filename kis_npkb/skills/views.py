from django.shortcuts import render
from django.views.generic import DetailView, ListView

from departments.models import Department
from employees.models import Employee
from .forms import SkillSortFilterForm
from .models import EmpSkill

# Create your views here.
#
# def group_sectors(a_queryset):
#     tmp_list = []
#     sector_id_list = a_queryset.distinct().order_by("sector_id").values_list("sector", flat=True)
#     for sector_id in sector_id_list:
#         internal_tmp_list = []
#         for emp_skill in a_queryset:
#             if emp_skill.sector.id ==sector_id:
#                 internal_tmp_list.append(emp_skill)
#         tmp_list.append(internal_tmp_list)

def group_sectors(a_queryset):
    """
    Получили queryset объектов EmpSkilllist.
    Для отображения в шаблоне нужны группировки сотрудников по секторам.
    """
    grouped_list = []
    sector_id_list = a_queryset.distinct().order_by("sector_id").values_list("sector", flat=True)
    for sector_id in sector_id_list:
        tmp_list = []
        for emp_skill in a_queryset:
            if emp_skill.sector.id == sector_id:
                tmp_list.append(emp_skill.employee)
        grouped_list.append(tmp_list)
    return grouped_list


class SkillListView(ListView):
    model = EmpSkill
    template_name = "skills/skill_list.html"
    ordering = 'sector_id'

    def get_queryset(self):
        queryset = EmpSkill.objects.all()
        department = self.request.GET.get("department")
        if department:
            queryset = queryset.filter(sector__department_id=department).order_by("sector")
        else:
            queryset = queryset.filter(sector__department_id=Department.objects.values_list("id", flat=True).first())
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["sort_filter_form"] = SkillSortFilterForm(self.request.GET)
        context_data["grouped_empskill_list"] = group_sectors(context_data.get('empskill_list'))
        return context_data


# отдельное вью под график