from django.contrib import admin
from .models import Employees, Positions

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class MyAdmin(TreeAdmin):
    list_display = ('position', 'last_name', 'first_name', 'date_employment',)
    form = movenodeform_factory(Employees)


admin.site.register(Employees, MyAdmin)
admin.site.register(Positions)