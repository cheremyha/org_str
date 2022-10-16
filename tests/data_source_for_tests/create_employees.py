"""
This code using in unit tests for create positions and employees.
"""

from app.models import Employees, Positions
from tests.data_source_for_tests.data_by_employees import employees_list, positions_list


def start_creating_employees():
    """
    Use this function to create employees for unit tests.
    """

    for position in positions_list:
        Positions.objects.create(position_name=position)

    print('Positions creation completed successfully')

    for employee in employees_list:
        cur_position_name = employee['position_name']
        position = Positions.objects.get(position_name=cur_position_name)

        # For SEO only ( it's root of graph so wee use add_root method ).
        if cur_position_name == 'Генеральный директор':
            seo = Employees.add_root(
                first_name=employee['first_name'],
                last_name=employee['last_name'],
                position=position,
                date_employment=employee['day'],
                salary=employee['salary'],
            )
            seo.refresh_from_db()
            seo_id = seo.id

            print('User SEO creation completed successfully')

        elif 'директор' in cur_position_name.lower():
            # Let`s create directors
            created_director = seo.add_child(first_name=employee['first_name'],
                                             last_name=employee['last_name'],
                                             position=position,
                                             date_employment=employee['day'],
                                             salary=employee['salary'], )

            created_director.refresh_from_db()

            info_message_str = 'Subordinate of {0} creation completed successfully, {1}'
            print(info_message_str.format(seo.position, created_director.position))

        elif cur_position_name == 'Руководитель группы':
            cto_position = Positions.objects.get(position_name='Технический директор')
            cto = Employees.objects.get(position_id=cto_position.id)

            # Let`s create team leaders.
            created_team_leader = cto.add_child(first_name=employee['first_name'],
                                                last_name=employee['last_name'],
                                                position=position,
                                                date_employment=employee['day'],
                                                salary=employee['salary'], )

            created_team_leader.refresh_from_db()

            info_message_str = 'Subordinate of {0} creation completed successfully, {1}'
            print(info_message_str.format(cto.position, created_team_leader.position))

        elif cur_position_name == 'Старший специалист':
            position_team_leader = Positions.objects.get(position_name='Руководитель группы')
            team_leader = Employees.objects.get(last_name='Прохоров',
                                                first_name='Пров',
                                                position_id=position_team_leader.id, )

            # Let`s create the senior specialists.
            created_senior_specialist = team_leader.add_child(first_name=employee['first_name'],
                                                              last_name=employee['last_name'],
                                                              position=position,
                                                              date_employment=employee['day'],
                                                              salary=employee['salary'], )

            created_senior_specialist.refresh_from_db()

            info_message_str = 'Subordinate of {0} creation completed successfully, {1}'
            print(info_message_str.format(team_leader.position, created_senior_specialist.position))

        elif cur_position_name == 'Специалист':
            position_senior_specialist = Positions.objects.get(position_name='Старший специалист')
            senior_specialist = Employees.objects.get(last_name='Зиновьев',
                                                      first_name='Аникей',
                                                      position_id=position_senior_specialist.id, )

            # Let`s create the middle specialists.
            created_middle_specialist = senior_specialist.add_child(first_name=employee['first_name'],
                                                                    last_name=employee['last_name'],
                                                                    position=position,
                                                                    date_employment=employee['day'],
                                                                    salary=employee['salary'], )

            created_middle_specialist.refresh_from_db()

            info_message_str = 'Subordinate of {0} creation completed successfully, {1}'
            print(info_message_str.format(senior_specialist.position, created_middle_specialist.position))

        elif cur_position_name == 'Младший специалист':
            position_middle_specialist = Positions.objects.get(position_name='Специалист')
            middle_specialist = Employees.objects.get(last_name='Никонова',
                                                      first_name='Марина',
                                                      position_id=position_middle_specialist.id, )

            # Let`s create the junior specialists.
            created_junior_specialist = middle_specialist.add_child(first_name=employee['first_name'],
                                                                    last_name=employee['last_name'],
                                                                    position=position,
                                                                    date_employment=employee['day'],
                                                                    salary=employee['salary'], )

            created_junior_specialist.refresh_from_db()

            info_message_str = 'Subordinate of {0} creation completed successfully, {1}'
            print(info_message_str.format(middle_specialist.position, created_junior_specialist.position))


if __name__ == '__main__':
    start_creating_employees()
    print('The test finished successfully')