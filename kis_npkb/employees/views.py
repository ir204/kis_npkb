
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from competences.models import EmpCompetence, Competence
from competences.service import competence_search
from skills.models import EmpSkill, Skill
from skills.service import skill_search
from .models import Employee
from departments.models import Department
from .forms import EmployeeSortFilterForm

# Create your views here.


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['object'] = self.object

        return self.render_to_response(context)


class EmployeeListView(View):

    def get_sort_filter_form(self, request):
        return {"sort_filter_form": EmployeeSortFilterForm(self.request.GET)}

    def get_context(self, request):
        context = self.get_sort_filter_form(request)

        usertext = self.request.GET.get("usertext")

        queryset_form = Employee.objects.all()  # objects for form
        queryset_employee = Employee.objects.all()  # objects for employee list

        department = self.request.GET.get("department")
        search_by = self.request.GET.get("search_by")
        fired = bool(self.request.GET.get("fired"))
        selected = self.request.GET.get("selected")
        selected_emp = self.request.GET.get("selected_emp")
        is_skill = bool(self.request.GET.get("is_skill"))

        if not fired:
            queryset_form = queryset_form.filter(fired=fired)

        if department:
            queryset_form = queryset_form.filter(sector__department_id=department)

        if search_by:
            if search_by == 'skill':
                queryset_form = queryset_form.filter(id__in=EmpSkill.objects.
                                                     filter(skill__name__icontains=usertext).
                                                     values_list("employee", flat=True))
            elif search_by == 'competence':
                queryset_form = queryset_form.filter(id__in=EmpCompetence.objects.
                                                     filter(competence__name__icontains=usertext).
                                                     values_list("employee", flat=True))
        else:
            if usertext:
                queryset_form = queryset_form.filter(Q(surname__icontains=usertext) |
                                                     Q(name__icontains=usertext) |
                                                     Q(patronymic__icontains=usertext))

        if not selected_emp:
            queryset_selected = queryset_employee.all().first()
        else:
            queryset_selected = queryset_employee.filter(id=selected_emp)

        if not selected:
            if is_skill:
                queryset_selected = EmpSkill.objects.filter(employee__id=queryset_selected.id)

                queryset_employee = queryset_employee.filter(id__in=EmpSkill.objects.
                                                             filter(skill__id=queryset_selected.
                                                                    values_list("id", flat=True).first()).
                                                             values_list("employee", flat=True))

            else:
                queryset_selected = EmpCompetence.objects.filter(employee__id=queryset_selected.id)

                queryset_employee = queryset_employee.filter(id__in=EmpCompetence.objects.
                                                             filter(competence__id=queryset_selected.
                                                                    values_list("id", flat=True).first()).
                                                             values_list("employee", flat=True))
        else:
            if is_skill:
                queryset_employee = queryset_employee.filter(id__in=EmpSkill.objects.
                                                             filter(skill__id=selected).
                                                             values_list("employee", flat=True))

                queryset_selected = EmpSkill.objects.filter(employee__id=queryset_selected.values_list("id", flat=True))

            else:
                queryset_employee = queryset_employee.filter(id__in=EmpCompetence.objects.
                                                             filter(competence__id=selected).
                                                             values_list("employee", flat=True))

                queryset_selected = EmpCompetence.objects.filter(employee__id=queryset_selected.
                                                                 values_list("id", flat=True))

        context['form_employee'] = queryset_form
        context['emp'] = queryset_employee
                    # 'selected_employee': queryset_selected[0].employee if len(queryset_selected) > 0 else None,
                    # }
        # queryset['competences'] = queryset["selected_employee"].empcompetence_set.all().values_list("competence__name", flat=True);
        return context

    def get(self, request):
        context = self.get_context(request)
        return render(request, "employees/employee_list.html", context)



# class EmployeeListView(ListView):
#     model = Employee
#     template_name = "employees/employee_list.html"
#
#     @property
#     def get_queryset(self):
#         usertext = self.request.GET.get("usertext")
#
#         queryset_form = Employee.objects.all()  # objects for form
#         queryset_employee = Employee.objects.all()  # objects for employee list
#
#         department = self.request.GET.get("department")
#         search_by = self.request.GET.get("search_by")
#         fired = bool(self.request.GET.get("fired"))
#         selected = self.request.GET.get("selected")
#         selected_emp = self.request.GET.get("selected_emp")
#         is_skill = bool(self.request.GET.get("is_skill"))
#
#         if not fired:
#             queryset_form = queryset_form.filter(fired=fired)
#
#         if department:
#             queryset_form = queryset_form.filter(sector__department_id=department)
#
#         if search_by:
#             if search_by == 'skill':
#                 queryset_form = queryset_form.filter(id__in=EmpSkill.objects.
#                                                      filter(skill__name__icontains=usertext).
#                                                      values_list("employee", flat=True))
#             elif search_by == 'competence':
#                 queryset_form = queryset_form.filter(id__in=EmpCompetence.objects.
#                                                      filter(competence__name__icontains=usertext).
#                                                      values_list("employee", flat=True))
#         else:
#             if usertext:
#                 queryset_form = queryset_form.filter(Q(surname__icontains=usertext) |
#                                                      Q(name__icontains=usertext) |
#                                                      Q(patronymic__icontains=usertext))
#
#         if not selected_emp:
#             queryset_selected = queryset_employee.all().first()
#         else:
#             queryset_selected = queryset_employee.filter(id=selected_emp)
#
#         if not selected:
#             if is_skill:
#                 queryset_selected = EmpSkill.objects.filter(employee__id=queryset_selected.id)
#
#                 queryset_employee = queryset_employee.filter(id__in=EmpSkill.objects.
#                                                              filter(skill__id=queryset_selected.
#                                                                     values_list("id", flat=True).first()).
#                                                              values_list("employee", flat=True))
#
#             else:
#                 queryset_selected = EmpCompetence.objects.filter(employee__id=queryset_selected.id)
#
#                 queryset_employee = queryset_employee.filter(id__in=EmpCompetence.objects.
#                                                              filter(competence__id=queryset_selected.
#                                                                     values_list("id", flat=True).first()).
#                                                              values_list("employee", flat=True))
#         else:
#             if is_skill:
#                 queryset_employee = queryset_employee.filter(id__in=EmpSkill.objects.
#                                                              filter(skill__id=selected).
#                                                              values_list("employee", flat=True))
#
#                 queryset_selected = EmpSkill.objects.filter(employee__id=queryset_selected.values_list("id", flat=True))
#
#             else:
#                 queryset_employee = queryset_employee.filter(id__in=EmpCompetence.objects.
#                                                              filter(competence__id=selected).
#                                                              values_list("employee", flat=True))
#
#                 queryset_selected = EmpCompetence.objects.filter(employee__id=queryset_selected.
#                                                                  values_list("id", flat=True))
#
#         queryset = {'form_employee': queryset_form,
#                     'emp': queryset_employee,
#                     'selected_employee': queryset_selected, }
#         return queryset

        # if search_by:
        #     if search_by == 'skill':
        #         search_by = EmpSkill.objects.all().filter(skill__name__icontains=usertext)
        #     elif search_by == 'competence':
        #         search_by = EmpCompetence.objects.all().filter(competence__name__icontains=usertext)
        #     queryset = queryset.filter(id=search_by.employee_id) # не работает
        # else:
        #     queryset = queryset.filter(Q(surname__icontains=usertext) |
        #                                Q(name__icontains=usertext) |
        #                                Q(patronymic__icontains=usertext)) # если пусто, не работает



        # if usertext:
        #     if search_by:
        #         if search_by == 'skill':
        #             form_queryset = skill_search(usertext)
        #         elif search_by == 'competence':
        #             form_queryset = competence_search(usertext)
        #     else:
        #         form_queryset = form_queryset.filter(surname__startswith=usertext)
        #     if not fired:
        #         form_queryset = Employee.sorted.all()
        #     if department:
        #         form_queryset = form_queryset.filter(department_id=department)
        # if not selected_emp:
        #     selected_emp = Employee.sorted.first()
        #     if not selected:
        #         selected = EmpCompetence.objects.filter(employee_id=selected_emp).first()
        # if is_skill:
        #     selected = EmpSkill.objects.filter(employee_id=selected_emp).first()
        #     queryset = EmpSkill.objects.filter(employee_id=selected_emp, skill_id=selected)
        # else:
        #     queryset = (EmpCompetence.objects.filter(employee_id=selected_emp))



    # def get(self, request, *args, **kwargs):
    #     context = super().get(request, *args, **kwargs)


        # form_queryset = Employee.objects.all()
        # queryset = Employee.objects.all()
        # usertext = self.request.GET.get("usertext")
        # department = self.request.GET.get("department")
        # search_by = self.request.GET.get("search_by")
        # fired = self.request.GET.get("fired")
        # selected = self.request.GET.get("selected")
        # selected_emp = self.request.GET.get("selected_emp")
        # is_skill = self.request.GET.get("is_skill")
        # if usertext:
        #     if search_by:
        #         if search_by == 'skill':
        #             form_queryset = skill_search(usertext)
        #         elif search_by == 'competence':
        #             form_queryset = competence_search(usertext)
        #     else:
        #         form_queryset = form_queryset.filter(surname__startswith=usertext)
        #     if not fired:
        #         form_queryset = Employee.sorted.all()
        #     if department:
        #         form_queryset = form_queryset.filter(department_id=department)
        # if not selected_emp:
        #     selected_emp = Employee.sorted.first()
        #     if not selected:
        #         selected = EmpCompetence.objects.filter(employee_id=selected_emp).first()
        # if is_skill:
        #     selected = EmpSkill.objects.filter(employee_id=selected_emp).first()
        #     queryset = EmpSkill.objects.filter(employee_id=selected_emp, skill_id=selected)
        # else:
        #     queryset = (EmpCompetence.objects.filter(employee_id=selected_emp))
        # return queryset

        # context['object_list'] = queryset
        # return self.render_to_response(context)



    # попробовать передалать под хоум вкладку с добавлением листов навыков внизу
    # попробовать реализовать поиск без перезагрузки(ajax(?))+отдельное вью под поиск
    # https://django.fun/qa/198489/ может быть полезно

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data["sort_filter_form"] = EmployeeSortFilterForm(self.request.GET)
    #     return context_data


class EmployeeHome(View):

    def get(self, request):
        return render(request, "employees/employee_home.html", {})


        #if usertext:
        #    if search_by:
        #        if search_by == 'skill':
        #            queryset = skill_search(usertext)
        #        elif search_by == 'competence':
        #            queryset = competence_search(usertext)
        #    else:
        #        queryset = queryset.filter(surname__startswith=usertext)
        #    if not fired:
        #        queryset = Employee.sorted.all()
        #    if department:
        #        queryset = queryset.filter(department_id=department)


class EmployeesByCompetenceListView(ListView):
    template_name = "employees/employees_by_competence.html"
    model = Employee

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        competence_id = self.kwargs.get("competence_id")
        employee_id = self.kwargs.get("employee_id")

        context = {"employees_by_competence": Employee.objects.filter(id__in=EmpCompetence.objects.
                                                                      filter(competence__id=competence_id).
                                                                      values_list("employee", flat=True)).
                                                                      exclude(id=employee_id)}
        return context


class EmployeesBySkillListView(ListView):
    template_name = "employees/employees_by_skill.html"
    model = Employee

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        skill_id = self.kwargs.get("skill_id")
        employee_id = self.kwargs.get("employee_id")

        context = {"employees_by_skill": Employee.objects.filter(id__in=EmpSkill.objects.
                                                                 filter(skill__id=skill_id).
                                                                 values_list("employee", flat=True)).
                                                                 exclude(id=employee_id)}
        return context


class CompetenceForEmployeeListView(ListView):
    template_name = "employees/competence_for_employee.html"
    model = EmpCompetence

    def get_context_data(self, **kwargs):
        employee_id = self.kwargs.get("employee_id")
        context = {"competence_for_employee": EmpCompetence.objects.filter(employee__id=employee_id)}
        return context


class SkillForEmployeeListView(ListView):
    template_name = "employees/skill_for_employee.html"
    model = EmpSkill

    def get_context_data(self, **kwargs):
        employee_id = self.kwargs.get("employee_id")
        context = {"skill_for_employee": EmpSkill.objects.filter(employee__id=employee_id)}
        return context
