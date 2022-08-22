""" Let`s create filters for paginated employees page. """
from django_filters import FilterSet
from .models import Employees


class EmployeesFilter(FilterSet):
    """ Define a filter. """
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'position')
