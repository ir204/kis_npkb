from .models import EmpCompetence
from employees.models import Employee


def competence_search(usertext):
    competence = EmpCompetence.objects.filter(competence__startswith=usertext)
    return competence.employee.all
