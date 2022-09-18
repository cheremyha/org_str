from django.contrib import admin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import Employees, Positions


class MyAdmin(TreeAdmin):
    list_display = ('position', 'last_name', 'first_name', 'date_employment',)
    form = movenodeform_factory(Employees)


admin.site.register(Employees, MyAdmin)
admin.site.register(Positions)