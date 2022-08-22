"""
Use these functions to seed(insert) fake data to database
Running this script is similar to executing the same code
as in the script in the shell console.
"""
from datetime import date
from faker import Faker
import random

from typing import Union, Optional
from django_connection import create_con
from django.db.models import Q

from app.models import Employees, Positions

# create connection from this script to Django project
create_con()








# Let`s localise Faker lib
fake = Faker('ru_RU')

# You can use this if everything is broken
# Employees.fix_tree()

# This method delete all data from model
# Employees.objects.all().delete()


def get_first_name() -> str:
    """
    :return: String with random first name.
    """
    first_name_ = fake.first_name()
    return first_name_


def get_last_name() -> str:
    """
    :return: String with random last name.
    """
    last_name_ = fake.last_name()
    return last_name_


def get_random_day() -> date:
    """
    :return: random day.
    """
    random_day_ = fake.date_this_year()
    return random_day_


def get_random_salary() -> float:
    """
    :return: Returns a random float number up to 2 decimal places == random salary
    """
    random_salary_ = round(random.uniform(80000, 600000), 2)

    return random_salary_


def get_position(name: str) -> Positions:
    """
    Function return an instance of a class Positions
    :param name: Name of position
    :return: Function return an instance of a class Positions
    """
    position_ = Positions.objects.get(position_name=name)
    return position_


def get_employee(employee_id: Optional[int] = None, position_id: Optional[int] = None) -> Employees:
    """
    Function return an instance of a class Employees
    :param employee_id: id of employee
    :param position_id: position_id of employee
    :return: Function return an instance of a class Employees
    """
    if employee_id:
        employee_ = Employees.objects.get(id=employee_id)
        return employee_

    employee_ = Employees.objects.get(position_id=position_id)
    return employee_


def created_seo() -> None:
    """
    This function creates SEO company == The initial vertex of the graph
    :return: None
    """
    # The position for which the employee is being created
    position = get_position('Генеральный директор')
    # Created random field
    day = get_random_day()
    salary = get_random_salary()
    first_name = get_first_name()
    last_name = get_last_name()

    seo = Employees.add_root(first_name=first_name,
                             last_name=last_name,
                             position=position,
                             date_employment=day,
                             salary=salary)
    seo.refresh_from_db()
    print('User SEO creation completed successfully')


def created_subordinate(chief_id: int, position_name: str) -> None:
    """
    This function create subordinate of the specified chief (chief_position)
    :param position_name: Name of the position for which the employee is being created
    :param chief_id: Еhe id of the chief of the employee(subordinate) being created
    :return: None
    """
    # Get object chief
    chief = Employees.objects.get(id=chief_id)
    # Get position for which the employee is being created
    position = get_position(position_name)
    # Created random field
    day = get_random_day()
    salary = get_random_salary()
    first_name = get_first_name()
    last_name = get_last_name()
    # Let`s create employee
    created_employee = chief.add_child(first_name=first_name,
                                       last_name=last_name,
                                       position=position,
                                       date_employment=day,
                                       salary=salary)

    created_employee.refresh_from_db()
    print(f'Subordinate of the chief_id =={chief_id} creation completed successfully, {created_employee.id}')


# Employees.objects.all().delete()

# Let`s create seo
created_seo()

seo_position_id = Positions.objects.all().filter(position_name='Генеральный директор').values('id')
seo_position_id = seo_position_id[0]['id']

seo_id = Employees.objects.all().filter(position_id=seo_position_id).values('id')
seo_id = seo_id[0]['id']


# Let`s create directors
created_subordinate(chief_id=seo_id, position_name='Технический директор')
created_subordinate(chief_id=seo_id, position_name='Директор по логистике')
created_subordinate(chief_id=seo_id, position_name='Операционный директор')
created_subordinate(chief_id=seo_id, position_name='Директор по аналитике')
created_subordinate(chief_id=seo_id, position_name='Директор по продукту')
created_subordinate(chief_id=seo_id, position_name='Директор по персоналу')
created_subordinate(chief_id=seo_id, position_name='Финансовый директор')
created_subordinate(chief_id=seo_id, position_name='Креативный директор')
created_subordinate(chief_id=seo_id, position_name='Директор по эффективности')
created_subordinate(chief_id=seo_id, position_name='Коммерческий директор')


# Get all directors from database
res = Positions.objects.all().filter(~Q(position_name='Генеральный директор'),
                                     position_name__contains='иректор').values('id')

# Let`s create team leaders
# Number of team leaders for each director
number_team_lead = 10
for cur_dir_pos_id in res:
    cur_dir_pos_id = cur_dir_pos_id['id']
    cur_dir = get_employee(position_id=cur_dir_pos_id)
    for _ in range(number_team_lead):
        created_subordinate(chief_id=cur_dir.id, position_name='Руководитель группы')


# Get all team leaders from database
# You must put current position_id for team lead position
all_tl = Employees.objects.all().filter(position_id=21).values('id')

# Let`s create a senior specialists
# Number of a senior specialists for each team leader ( team leader == tl )
number_senior_specialists = 10
for cur_tl_id in all_tl:
    cur_tl_id = cur_tl_id['id']
    cur_tl = get_employee(employee_id=cur_tl_id)
    for _ in range(number_senior_specialists):
        created_subordinate(chief_id=cur_tl.id, position_name='Старший специалист')


# Get all senior specialist from database
# You must put current position_id for senior specialist position
all_seniors = Employees.objects.all().filter(position_id=22).values('id')

# Let`s create middle specialists
# Number of middle specialists for each senior specialist ( specialist == ss )
number_middle_specialists = 15
for cur_ss_id in all_seniors:
    cur_ss_id = cur_ss_id['id']
    cur_ss = get_employee(employee_id=cur_ss_id)
    for _ in range(number_middle_specialists):
        created_subordinate(chief_id=cur_ss.id, position_name='Специалист')


# Let`s create junior specialists
# Number of junior specialists for each senior specialist ( junior specialists == js )
number_junior_specialists = 5
for cur_ss_id in all_seniors:
    cur_ss_id = cur_ss_id['id']
    cur_ss = get_employee(employee_id=cur_ss_id)
    for _ in range(number_junior_specialists):
        created_subordinate(chief_id=cur_ss.id, position_name='Младший специалист')
