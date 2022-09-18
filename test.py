from decimal import getcontext, Decimal
from django_connection import create_con
from app.forms import EmployeesUpdateForm
from app.models import Positions, Employees

#
# create_con()
#
# form = EmployeesUpdateForm()
# for field in form:
#     print(field)

# Get object from database.
employee = Employees.objects.get(id=118921)
# Get position_id this object ( from Employees table )
position_id_employees = employee.position
print(employee.position_id)





