from django.contrib import admin

from skills.models import EmpSkill, Skill

# Register your models here.


admin.site.register(Skill)
admin.site.register(EmpSkill)
