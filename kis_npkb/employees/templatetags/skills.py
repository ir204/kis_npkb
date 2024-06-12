import datetime
from django import template

from employees.models import Employee
from skills.models import EmpSkill

register = template.Library()


@register.simple_tag
def get_skill_table(employee_id):
    skill_levels = EmpSkill.objects.filter(employee__id=employee_id)
    names = Employee.objects.filter(id=employee_id)
    template_table = '<tr>'
    style = ''
    for name in names:
        template_table += '<td>%s, %s</td>' % (name.full_name, name.post)
        for empskills in skill_levels:
            if not empskills.skill_level:
                style = 'red',
                empskills.skill_level = '0'
            elif empskills.skill_level == 1:
                style = 'orange'
            elif empskills.skill_level == 2:
                style = 'yellow'
            elif empskills.skill_level == 3:
                style = 'lime'
            elif empskills.skill_level == 4:
                style = 'green'
            template_table += '<td class="font-weight-bold" style="background-color: %s> %s </td>' % (style, empskills.skill_level)
        template_table += '</tr>'
    return template_table
