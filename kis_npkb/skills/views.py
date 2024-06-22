from django.views.generic import ListView

from departments.models import Department, Sector
from employees.models import Employee
from .forms import SkillSortFilterForm, SkillTableSortFilterForm
from .models import EmpSkill, Skill


def group_sectors(a_queryset):
    """
    Получили queryset объектов EmpSkilllist.
    Для отображения в шаблоне нужны группировки сотрудников по секторам.
    """
    grouped_list = []
    sector_id_list = a_queryset.distinct().order_by("sector_id").values_list("sector", flat=True)
    for sector_id in sector_id_list:
        tmp_set = set()
        for emp_skill in a_queryset:
            if emp_skill.sector.id == sector_id:
                tmp_set.add(emp_skill.employee)
        grouped_list.append(list(tmp_set))
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


class SkillTableListView(ListView):
    model = EmpSkill
    template_name = "skills/skills_table_list.html"

    def get_queryset(self):
        queryset = EmpSkill.objects.all()
        sector = self.request.GET.get("sector")
        if sector:
            queryset = queryset.filter(sector__id=sector).order_by("sector").distinct()
        else:
            queryset = queryset.filter(sector__id=Sector.objects.values_list("id", flat=True).first()).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = SkillTableSortFilterForm(self.request.GET)
        return context_data


class EmployeesBySkillTableListView(ListView):
    template_name = "skills/employees_by_skill_table.html"
    model = Employee

    def get_context_data(self, **kwargs):
        skill_id = self.kwargs.get("skill_id")
        sector_id = self.kwargs.get("sector_id")

        context = {"employees_by_skill": Employee.objects.filter(id__in=EmpSkill.objects.
                                                                 filter(skill__id=skill_id, sector__id=sector_id).
                                                                 values_list("employee", flat=True)),
                   "skill": Skill.objects.filter(id=skill_id).values_list("name", flat=True)}
        return context

