from django.urls import path

from competences.views import CompetenceTableListView, EmployeesByCompetenceTableListView


urlpatterns = [
    path("competence-table/", CompetenceTableListView.as_view(), name="competence-table-list"),
    path("employees-by-competence-table/<int:competence_id>/<int:sector_id>", EmployeesByCompetenceTableListView.as_view(),
         name="employee-by-competence-table"),
]