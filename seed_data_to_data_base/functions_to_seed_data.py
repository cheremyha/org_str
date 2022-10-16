"""
Use these functions to seed(insert) fake data to database
Running this script is similar to executing the same code
as in the script in the shell console.
"""
from datetime import date
from faker import Faker
import random

from typing import Optional
from seed_data_to_data_base.django_connection import create_con
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