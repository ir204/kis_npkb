"""
URL configuration for kis_npkb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from competences.views import CompetenceListView
from employees.views import (EmployeeListView, EmployeeDetailView, EmployeesByCompetenceListView,
                             CompetenceForEmployeeListView, SkillForEmployeeListView, EmployeesBySkillListView)    # EmployeeHome
from skills.views import SkillListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/", EmployeeListView.as_view(), name="employee-list"),
    path("employee/<int:pk>", EmployeeDetailView.as_view(), name="employee-detail"),
    path("employees-by-competence/<int:competence_id>", EmployeesByCompetenceListView.as_view(), name="employees-by-competence"),
    path("employees-by-skill/<int:skill_id>", EmployeesBySkillListView.as_view(), name="employees-by-skill"),
    path("competence-for-employee/<int:employee_id>", CompetenceForEmployeeListView.as_view(), name="competence-for-employee"),
    path("skill-for-employee/<int:employee_id>", SkillForEmployeeListView.as_view(), name="skill-for-employee"),

    path("competence/", CompetenceListView.as_view(), name="competence-list"),
    path("competence/chart", EmployeeDetailView.as_view(), name="competence-chart"),

    path("skill/", SkillListView.as_view(), name="skill-list"),
    path("skill/chart", EmployeeDetailView.as_view(), name="skill-chart"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
