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
    """ This view for dynamic tree page with menu. """
    template = loader.get_template('app/dynamic_tree_page_with_menu.html')
    annotated_list = Employees.get_annotated_list()
    context = {'annotated_list': annotated_list}
    return HttpResponse(template.render(context, request))

class EmployeeCreateView(LoginRequiredMixin, ListView):
    """ This view for the new employee creation page. """

    # Create data for GET request using class attributes and function get_context_data.

    # Create data about positions using class attributes
    model = Positions
    template_name = 'app/create_employee.html'
    context_object_name = 'positions'

    # Create data about positions function get_context_data
    def get_context_data(self, **kwargs):
        """
        Let's redefine method get_context_data to send data
        from model Employees to the template.
        This will allow you to send more data,
        from two models Positions and Employees at the same time.
        """
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context.update({'employees_list': Employees.get_annotated_list()})
        return context

    def post(self, request):
        """
        We take the values for the new employee
        from the POST request sent to the server.
        """

        # We get the data from the POST request and write them to variables:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        position_id = request.POST['position_id']
        date_employment = request.POST['date_employment']
        salary = request.POST['salary']
        chief_id = request.POST['chief_id']

        # Get instances classes, it`s necessary to create new employee
        position = Positions.objects.get(id=position_id)
        chief = Employees.objects.get(id=chief_id)

        created_employee = chief.add_child(first_name=first_name,
                                           last_name=last_name,
                                           position=position,
                                           date_employment=date_employment,
                                           salary=salary)

        created_employee.refresh_from_db()

        template = loader.get_template('app/successful_addition.html')
        context = {'created_employee': created_employee}

        # If a new employee is successfully added, then we display a message to the user about this not
        return HttpResponse(template.render(context, request))
