"""
This data is data source for test_views unit test.
test_views unit test use this data for
create tests objects in test database when unit test is running.
"""
from typing import Union, Optional


# Create positions for tests.
positions_list = [
    'Генеральный директор',
    'Технический директор',
    'Директор по логистике',
    'Операционный директор',
    'Директор по аналитике',
    'Директор по продукту',
    'Директор по персоналу',
    'Финансовый директор',
    'Креативный директор',
    'Директор по эффективности',
    'Коммерческий директор',
    'Руководитель группы',
    'Старший специалист',
    'Специалист',
    'Младший специалист',
]

# Let's define fields for test objects.
# It must be at the same in each test running.
# Following data is defined in the appropriate order graph.
employees_list = [
    dict(
        position_name='Генеральный директор',
        day='2022-01-17',
        salary=573475.72,
        first_name='Филарет',
        last_name='Алексеева'
    ),
    dict(
        position_name='Технический директор',
        day='2022-02-16',
        salary=107075.43,
        first_name='Кузьма',
        last_name='Мельников'
    ),
    dict(
        position_name='Руководитель группы',
        day='2022-03-12',
        salary=361587.16,
        first_name='Пров',
        last_name='Прохоров'
    ),
    dict(
        position_name='Старший специалист',
        day='2022-06-13',
        salary=409340.87,
        first_name='Аникей',
        last_name='Зиновьев'
    ),
    dict(
        position_name='Специалист',
        day='2022-04-13',
        salary=148706.58,
        first_name='Марина',
        last_name='Никонова'
    ),
    dict(
        position_name='Младший специалист',
        day='2022-04-11',
        salary=565367.73,
        first_name='Амвросий',
        last_name='Блинова'
    ),
    dict(
        position_name='Младший специалист',
        day='2022-09-24',
        salary=465288.37,
        first_name='Агап',
        last_name='Ермакова'
    ),
    dict(
        position_name='Специалист',
        day='2022-04-15',
        salary=377797.01,
        first_name='Борис',
        last_name='Буров'
    ),
    dict(
        position_name='Специалист',
        day='2022-03-15',
        salary=387797.01,
        first_name='Андрей',
        last_name='Буровчик'
    ),
    dict(
        position_name='Специалист',
        day='2022-03-05',
        salary=787797.01,
        first_name='Андрей',
        last_name='Петров'
    ),
    dict(
        position_name='Специалист',
        day='2022-03-01',
        salary=787797.01,
        first_name='Андрей',
        last_name='Козачек'
    ),
    dict(
        position_name='Специалист',
        day='2022-03-01',
        salary=787797.01,
        first_name='Аркадий',
        last_name='Кобяков'
    ),
    dict(
        position_name='Старший специалист',
        day='2022-04-07',
        salary=460309.62,
        first_name='Прохор',
        last_name='Суханов'
    ),
    dict(
        position_name='Руководитель группы',
        day='2022-08-04',
        salary=358347.4,
        first_name='Елисей',
        last_name='Архипов'
    ),
    dict(
        position_name='Руководитель группы',
        day='2022-01-27',
        salary=501236.09,
        first_name='Авксентий',
        last_name='Бобылева'
    ),
    dict(
        position_name='Директор по логистике',
        day='2022-02-10',
        salary=335496.75,
        first_name='Савватий',
        last_name='Полякова'
    ),
    dict(
        position_name='Операционный директор',
        day='2022-03-04',
        salary=231328.49,
        first_name='Маргарита',
        last_name='Власов'
    ),
    dict(
        position_name='Директор по аналитике',
        day='2022-06-28',
        salary=148457.2,
        first_name='Аполлинарий',
        last_name='Владимиров'
    ),
    dict(
        position_name='Директор по продукту',
        day='2022-02-10',
        salary=291017.46,
        first_name='Олимпиада',
        last_name='Трофимов'
    ),
    dict(
        position_name='Директор по персоналу',
        day='2022-07-12',
        salary=194796.61,
        first_name='Севастьян',
        last_name='Иванова'
    ),
    dict(
        position_name='Финансовый директор',
        day='2022-05-17',
        salary=597612.79,
        first_name='Ираклий',
        last_name='Симонова'
    ),
    dict(
        position_name='Креативный директор',
        day='2022-07-18',
        salary=252076.51,
        first_name='Геннадий',
        last_name='Никифоров'
    ),
    dict(
        position_name='Директор по эффективности',
        day='2022-08-10',
        salary=80639.56,
        first_name='Спиридон',
        last_name='Королева'
    ),
    dict(
        position_name='Коммерческий директор',
        day='2022-09-12',
        salary=395145.89,
        first_name='Софон',
        last_name='Макаров'
    ),
]

graph_data_list = [
    {'last_name_first_name': 'Алексеева_Филарет', 'graph_data': {'open': True, 'close': [], 'level': 0}},
    {'last_name_first_name': 'Мельников_Кузьма', 'graph_data': {'open': True, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Прохоров_Пров', 'graph_data': {'open': True, 'close': [], 'level': 2}},
    {'last_name_first_name': 'Зиновьев_Аникей', 'graph_data': {'open': True, 'close': [], 'level': 3}},
    {'last_name_first_name': 'Никонова_Марина', 'graph_data': {'open': True, 'close': [], 'level': 4}},
    {'last_name_first_name': 'Блинова_Амвросий', 'graph_data': {'open': True, 'close': [], 'level': 5}},
    {'last_name_first_name': 'Ермакова_Агап', 'graph_data': {'open': False, 'close': [0], 'level': 5}},
    {'last_name_first_name': 'Буров_Борис', 'graph_data': {'open': False, 'close': [], 'level': 4}},
    {'last_name_first_name': 'Буровчик_Андрей', 'graph_data': {'open': False, 'close': [], 'level': 4}},
    {'last_name_first_name': 'Петров_Андрей', 'graph_data': {'open': False, 'close': [], 'level': 4}},
    {'last_name_first_name': 'Козачек_Андрей', 'graph_data': {'open': False, 'close': [], 'level': 4}},
    {'last_name_first_name': 'Кобяков_Аркадий', 'graph_data': {'open': False, 'close': [0], 'level': 4}},
    {'last_name_first_name': 'Суханов_Прохор', 'graph_data': {'open': False, 'close': [0], 'level': 3}},
    {'last_name_first_name': 'Архипов_Елисей', 'graph_data': {'open': False, 'close': [], 'level': 2}},
    {'last_name_first_name': 'Бобылева_Авксентий', 'graph_data': {'open': False, 'close': [0], 'level': 2}},
    {'last_name_first_name': 'Полякова_Савватий', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Власов_Маргарита', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Владимиров_Аполлинарий', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Трофимов_Олимпиада', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Иванова_Севастьян', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Симонова_Ираклий', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Никифоров_Геннадий', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Королева_Спиридон', 'graph_data': {'open': False, 'close': [], 'level': 1}},
    {'last_name_first_name': 'Макаров_Софон', 'graph_data': {'open': False, 'close': [0, 1], 'level': 1}},
]


# This function don't use in project now, but it may be needed in the futureю
def get_employee(employees_list: list,
                 first_name: str,
                 last_name: str,
                 position_name: str) -> Optional[Union[dict, bool]]:
    """
    Use this function to found employee in employees_list
    :param employees_list: list with all testing employees
    :param first_name: the first name of the employee to be found
    :param last_name: the last name of the employee to be found
    :param position_name: the position name of the employee to be found
    :return: dict with data by employee if the employee will be found
    and None if employee will not be found.
    """
    for employee in employees_list:

        # Compare current value from employees_list with data
        condition_last_name = employee['last_name'] == last_name
        condition_first_name = employee['first_name'] == first_name
        condition_position = employee['position_name'] == position_name

        condition_list = [condition_last_name, condition_first_name, condition_position]

        if all(condition_list):
            return employee


if __name__ == '__main__':
    # This code as like little unit tests.

    # The function must found employee in employees_list in this case.
    res_successful_search = get_employee(employees_list=employees_list,
                                         first_name='Агап',
                                         last_name='Ермакова',
                                         position_name='Младший специалист',)
    print(res_successful_search)

    # The function should not find employee in employees_list in this case.
    res_unsuccessful_search = get_employee(employees_list=employees_list,
                                           first_name='Агап',
                                           last_name='рмакова',
                                           position_name='Младший специалист',)
    print(res_unsuccessful_search)

    print('The test finished successfully')





