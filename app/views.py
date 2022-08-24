""" Let`s create different views for employees"""
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employees, Positions
from .filters import EmployeesFilter


def static_tree_page_view(request):
    """ This view for page with static employee tree """
    template = loader.get_template('app/static_tree_page.html')
    annotated_list = Employees.get_annotated_list()
    context = {'annotated_list': annotated_list}
    return HttpResponse(template.render(context, request))


class EmployeesPaginator(LoginRequiredMixin, ListView):
    """ This is the view for the paginated employees page. """
    model = Employees
    template_name = 'app/paginated_page_with_employees.html'
    context_object_name = 'employees'
    ordering = ['depth']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        """ This method is necessary for filtering on the page. """
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeesFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        """ This method is necessary for pagination on the page. """
        queryset = super().get_queryset()
        return EmployeesFilter(self.request.GET, queryset=queryset).qs


def dynamic_tree_page_view(request):
    """ This view for new dynamic tree page with menu. """
    template = loader.get_template('app/dynamic_tree_page_with_menu.html')
    annotated_list = Employees.get_annotated_list()
    context = {'annotated_list': annotated_list}
    return HttpResponse(template.render(context, request))

