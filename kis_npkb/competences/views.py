from django.shortcuts import render
from django.views.generic import DetailView, ListView

from departments.models import Sector
from employees.models import Employee
from .forms import CompetenceSortFilterForm, CompetenceTableSortFilterForm
from .models import EmpCompetence, Competence


# Create your views here.


class CompetenceTableListView(ListView):
    model = EmpCompetence
    template_name = "competences/competences_table_list.html"

    def get_queryset(self):
        queryset = EmpCompetence.objects.all()
        sector = self.request.GET.get("sector")
        if sector:
            queryset = queryset.filter(sector__id=sector).order_by("sector").distinct()
        else:
            queryset = queryset.filter(sector__id=Sector.objects.values_list("id", flat=True).first()).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = CompetenceTableSortFilterForm(self.request.GET)
        return context_data


class EmployeesByCompetenceTableListView(ListView):
    template_name = "competences/employees_by_competence_table.html"
    model = Employee

    def get_context_data(self, **kwargs):
        competence_id = self.kwargs.get("competence_id")
        sector_id = self.kwargs.get("sector_id")

        context = {"employees_by_competence": Employee.objects.filter(id__in=EmpCompetence.objects.
                                                                      filter(competence__id=competence_id,
                                                                             sector__id=sector_id).
                                                                      values_list("employee", flat=True))}
        return context

    # отдельное вью под график