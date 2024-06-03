from .models import EmpSkill


def skill_search(usertext):
    skill = EmpSkill.objects.filter(skill__startswith=usertext)
    return skill.employee.all
