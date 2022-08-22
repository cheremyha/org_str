from django.db import models
from treebeard.mp_tree import MP_Node


class Positions(models.Model):
    position_name = models.CharField(max_length=30, verbose_name='Должность')

    def __str__(self):
        return '{}'.format(self.position_name)

    class Meta:
        verbose_name_plural = 'Должности в компании'
        verbose_name = 'Должность'


class Employees(MP_Node):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    position = models.ForeignKey('Positions', on_delete=models.PROTECT,
                                 verbose_name='Должность')
    date_employment = models.DateField(verbose_name='Дата трудоустройства')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    node_order_by = ['position']

    def __str__(self):
        return 'Employee: {}'.format(self.position)

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'








