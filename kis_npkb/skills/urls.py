from django.urls import path

from skills.views import SkillListView, SkillTableListView, EmployeesBySkillTableListView

urlpatterns = [
    path("", SkillListView.as_view(), name="skill-list"),

    path("skill-table/", SkillTableListView.as_view(), name="skill-table-list"),
    path("employees-by-skill-table/<int:skill_id>/<int:sector_id>", EmployeesBySkillTableListView.as_view(),
         name="employee-by-skill-table")
]