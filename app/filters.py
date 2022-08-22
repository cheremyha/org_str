from django_filters import FilterSet
from .models import Employees


class EmployeesFilter(FilterSet):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'position')
