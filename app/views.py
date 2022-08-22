from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employees, Positions
from .filters import EmployeesFilter


def show_employees(request):
    template = loader.get_template('app/employees_list.html')
    annotated_list = Employees.get_annotated_list()
    context = {'annotated_list': annotated_list}
    return HttpResponse(template.render(context, request))


class EmployeesPaginator(LoginRequiredMixin, ListView):
    model = Employees
    template_name = 'app/employees_with_paginate.html'
    context_object_name = 'employees'
    ordering = ['depth']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeesFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return EmployeesFilter(self.request.GET, queryset=queryset).qs


def tree_menu(request):
    template = loader.get_template('app/tree_menu.html')
    annotated_list = Employees.get_annotated_list()
    context = {'annotated_list': annotated_list}
    return HttpResponse(template.render(context, request))

