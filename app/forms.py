from treebeard.forms import MoveNodeForm
from .models import Employees


class EmployeesUpdateForm(MoveNodeForm):
    class Meta:
        model = Employees
        fields = [
            'first_name',
            'last_name',
            'position',
            'date_employment',
            'salary',
        ]
        # exclude = ('sib_order', 'parent')
