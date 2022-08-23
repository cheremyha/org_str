""" Let`s create models for employees and position"""
from django.db import models
from treebeard.mp_tree import MP_Node


class Positions(models.Model):
    """ Create entity for positions, e.g. chief technology officer. """
    position_name = models.CharField(max_length=30, verbose_name='Должность')

    def __str__(self):
        """
        Let's change the display of model instances
        on the administrator's site.
        """
        return '{}'.format(self.position_name)

    class Meta:
        """ Let's change the name of position model in the admin site. """
        verbose_name_plural = 'Должности в компании'
        verbose_name = 'Должность'


class Employees(MP_Node):
    """ Created entity for employees, e.g. Ivan Ivanov or John Smith. """
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    position = models.ForeignKey('Positions', on_delete=models.PROTECT,
                                 verbose_name='Должность')
    date_employment = models.DateField(verbose_name='Дата трудоустройства')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    node_order_by = ['position']

    def __str__(self):
        """
        Let's change the display of model instances
        on the administrator's site.
        """
        return 'Employee: {}'.format(self.position)

    class Meta:
        """ Let's change the name of position model in the admin site. """
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'








