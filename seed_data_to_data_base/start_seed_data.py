"""
Start this code to seed data into database.
"""

from functions_to_seed_data import *
from tests.data_source_for_tests.data_by_employees import positions_list


# Delete all old data from Database.
Employees.objects.all().delete()
Positions.objects.all().delete()

for position in positions_list:
    Positions.objects.create(position_name=position)

print('Positions creation completed successfully')

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

tl_position = Positions.objects.get(position_name='Руководитель группы')
all_tl = Employees.objects.all().filter(position_id=tl_position.id).values('id')

# Let`s create a senior specialists
# Number of a senior specialists for each team leader ( team leader == tl )
number_senior_specialists = 6
for cur_tl_id in all_tl:
    cur_tl_id = cur_tl_id['id']
    cur_tl = get_employee(employee_id=cur_tl_id)
    for _ in range(number_senior_specialists):
        created_subordinate(chief_id=cur_tl.id, position_name='Старший специалист')


# Get all senior specialist from database

senior_position = Positions.objects.get(position_name='Старший специалист')
all_seniors = Employees.objects.all().filter(position_id=senior_position.id).values('id')

# Let`s create middle specialists
# Number of middle specialists for each senior specialist ( specialist == ss )
number_middle_specialists = 4
for cur_ss_id in all_seniors:
    cur_ss_id = cur_ss_id['id']
    cur_ss = get_employee(employee_id=cur_ss_id)
    for _ in range(number_middle_specialists):
        created_subordinate(chief_id=cur_ss.id, position_name='Специалист')

# Let`s create junior specialists
# Number of junior specialists for each senior specialist ( junior specialists == js )
number_junior_specialists = 2
for cur_ss_id in all_seniors:
    cur_ss_id = cur_ss_id['id']
    cur_ss = get_employee(employee_id=cur_ss_id)
    for _ in range(number_junior_specialists):
        created_subordinate(chief_id=cur_ss.id, position_name='Младший специалист')