from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .forms import CompetenceSortFilterForm
from .models import EmpCompetence


# Create your views here.


class CompetenceListView(ListView):
    model = EmpCompetence
    template_name = "competences/competence_list.html"

    def get_queryset(self):
        queryset = EmpCompetence.objects.all()
        department = self.request.GET.get("department")
        if department:
            queryset = queryset.filter(sector_department=department)
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["sort_filter_form"] = CompetenceSortFilterForm(self.request.GET)
        return context_data

    # отдельное вью под график