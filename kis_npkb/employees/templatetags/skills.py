import datetime
from django import template
from django.utils.safestring import mark_safe

from employees.models import Employee
from skills.models import EmpSkill, Skill

register = template.Library()


@register.simple_tag
def get_skills(employee):

    sector_skills = employee.sector.empskill_set.distinct().order_by("skill").values_list("skill__name", flat=True)
    employee_skills_with_levels = list(employee.empskill_set.order_by("skill__name").values_list("skill__name", "skill_level"))
    style = ''
    template_table = ''


    """
    Цикл по скилам сектора
        Уровень скила = 0
        Цикл по скилам сотрудника
            Если скил сотрудника = скилу сектора:
                Уровень скила = Уровень скила сотрудника
                Перварть цикл
    """

    for sector_skill in sector_skills:
        skill_level = 0
        for empskill in employee_skills_with_levels:
            if empskill[0] == sector_skill:
                skill_level = empskill[1]
        if not skill_level:
            style = 'red'
        elif skill_level == 1:
            style = 'orange'
        elif skill_level == 2:
            style = 'yellow'
        elif skill_level == 3:
            style = 'lime'
        elif skill_level == 4:
            style = '#17a917'
        template_table += '<td class="font-weight-bold" style="background-color: %s;"> %s </td>' % (style, skill_level)
    return mark_safe(template_table)



@register.simple_tag
def handle_group(employee):
    sector_skills = employee.sector.empskill_set.distinct().order_by("skill").values_list("skill__name", flat=True)
    template_table = '<thead class="align-middle table-info"><tr><th></th>'
    for sector_skill in sector_skills:
        template_table += '<th scope="col">%s</th>' % sector_skill
    template_table += '</tr></thead>'
    return mark_safe(template_table)
