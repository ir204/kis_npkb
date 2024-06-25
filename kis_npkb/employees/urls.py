from django.urls import path

from employees.views import (EmployeeListView, EmployeeDetailView, EmployeesByCompetenceListView,
                             CompetenceForEmployeeListView, SkillForEmployeeListView, EmployeesBySkillListView)


urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("employee/<int:pk>", EmployeeDetailView.as_view(), name="employee-detail"),

    path("employees-by-competence/<int:competence_id>/<int:employee_id>", EmployeesByCompetenceListView.as_view(),
         name="employees-by-competence"),
    path("employees-by-skill/<int:skill_id>/<int:employee_id>", EmployeesBySkillListView.as_view(),
         name="employees-by-skill"),

    path("competence-for-employee/<int:employee_id>", CompetenceForEmployeeListView.as_view(),
         name="competence-for-employee"),
    path("skill-for-employee/<int:employee_id>", SkillForEmployeeListView.as_view(), name="skill-for-employee"),
]