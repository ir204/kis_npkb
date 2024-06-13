
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from competences.models import EmpCompetence, Competence
from competences.service import competence_search
from skills.models import EmpSkill, Skill
from skills.service import skill_search
from .models import Employee
from departments.models import Department
from .forms import EmployeeSortFilterForm

# Create your views here.


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['object'] = self.object

        return self.render_to_response(context)


class EmployeeListView(View):

    def get_sort_filter_form(self, request):
        return {"sort_filter_form": EmployeeSortFilterForm(self.request.GET)}

    def get_context(self, request):
        context = self.get_sort_filter_form(request)

        usertext = self.request.GET.get("usertext")

        queryset_form = Employee.objects.all()  # objects for for

        department = self.request.GET.get("department")
        search_by = self.request.GET.get("search_by")
        fired = bool(self.request.GET.get("fired"))

        if not fired:
            queryset_form = queryset_form.filter(fired=fired)

        if department:
            queryset_form = queryset_form.filter(sector__department_id=department)

        if search_by:
            if search_by == 'skill':
                queryset_form = queryset_form.filter(id__in=EmpSkill.objects.
                                                     filter(skill__name__icontains=usertext).
                                                     values_list("employee", flat=True))
            elif search_by == 'competence':
                queryset_form = queryset_form.filter(id__in=EmpCompetence.objects.
                                                     filter(competence__name__icontains=usertext).
                                                     values_list("employee", flat=True))
        else:
            if usertext:
                queryset_form = queryset_form.filter(Q(surname__icontains=usertext) |
                                                     Q(name__icontains=usertext) |
                                                     Q(patronymic__icontains=usertext))

        context['form_employee'] = queryset_form
        return context

    def get(self, request):
        context = self.get_context(request)
        return render(request, "employees/employee_list.html", context)






class EmployeeHome(View):

    def get(self, request):
        return render(request, "employees/employee_home.html", {})



class EmployeesByCompetenceListView(ListView):
    template_name = "employees/employees_by_competence.html"
    model = Employee

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        competence_id = self.kwargs.get("competence_id")
        employee_id = self.kwargs.get("employee_id")

        context = {"employees_by_competence": Employee.objects.filter(id__in=EmpCompetence.objects.
                                                                      filter(competence__id=competence_id).
                                                                      values_list("employee", flat=True)).
                                                                      exclude(id=employee_id),
                   "competence": EmpCompetence.objects.filter(competence_id=competence_id).first()}
        return context


class EmployeesBySkillListView(ListView):
    template_name = "employees/employees_by_skill.html"
    model = Employee

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        skill_id = self.kwargs.get("skill_id")
        employee_id = self.kwargs.get("employee_id")

        context = {"employees_by_skill": Employee.objects.filter(id__in=EmpSkill.objects.
                                                                 filter(skill__id=skill_id).
                                                                 values_list("employee", flat=True)).
                                                                 exclude(id=employee_id),
                   "skill": EmpSkill.objects.filter(skill__id=skill_id).first()}
        return context


class CompetenceForEmployeeListView(ListView):
    template_name = "employees/competence_for_employee.html"
    model = EmpCompetence

    def get_context_data(self, **kwargs):
        employee_id = self.kwargs.get("employee_id")
        context = {"competence_for_employee": EmpCompetence.objects.filter(employee__id=employee_id).order_by("-competence_level")}
        return context


class SkillForEmployeeListView(ListView):
    template_name = "employees/skill_for_employee.html"
    model = EmpSkill

    def get_context_data(self, **kwargs):
        employee_id = self.kwargs.get("employee_id")
        context = {"skill_for_employee": EmpSkill.objects.filter(employee__id=employee_id).order_by("-skill_level")}
        return context
