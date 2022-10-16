"""
This code is unit test for views.
You can run these tests only, using command in terminal:
python manage.py test tests.test_views --verbosity 2
"""
from datetime import datetime
from decimal import Decimal

from django.test import TestCase
from tests.data_source_for_tests.create_employees import start_creating_employees
from tests.data_source_for_tests.data_by_employees import employees_list, graph_data_list


class EmployeesListViewTest(TestCase):
    """
    This set up create 24 employees using data from datasource_for_tests directory.
    """
    @classmethod
    def setUpTestData(cls):

        start_creating_employees()

    def test_static_tree_page_view(self):
        """
        This test do check for static_tree_page_view.
        It checks:
            - Status code this page
            - Using template
            - And almost data from page context.
        """
        resp = self.client.get('/static_tree_page/')

        # Get page context.
        page_context = resp.context['annotated_list']

        # Check status code.
        self.assertEqual(resp.status_code, 200)

        # Check using templates.
        self.assertTemplateUsed(resp, 'app/static_tree_page.html')

        # Check that the length employees_list from datasource
        # is at the same as employees_list from static_tree_page_view.
        self.assertEqual(len(employees_list), len(page_context))

        # Let's create union_employees_list, each element of which is a tuple.
        # The first tuple element employees_list[x], is employee data from datasource.
        # The second tuple element page_context[x], is employee data from static_tree_page_view.
        # The third tuple element graph_data_list[x], is employee data from datasource (graph_data_list).
        union_employees_list = [
            (employees_list[x], graph_data_list[x], page_context[x]) for x in range(len(employees_list))
        ]

        for employee in union_employees_list:

            # Data by current employee from datasource ( == ds )
            employee_ds = employee[0]

            # Get employee fields from datasource.
            position_name_ds = employee_ds['position_name']
            day_ds = employee_ds['day']
            salary_ds = employee_ds['salary']
            first_name_ds = employee_ds['first_name']
            last_name_ds = employee_ds['last_name']

            # Convert day in string format to datetime format.
            day_ds = datetime.strptime(day_ds, '%Y-%m-%d').date()

            # Convert salary_ds from float to decimal.
            salary_ds = Decimal(str(salary_ds))

            # Get employee fields from datasource (graph_data_list == gd).
            employee_gd = employee[1]['graph_data']
            open_gd_ds = employee_gd['open']
            close_gd_ds = employee_gd['close']
            level_gd_ds = employee_gd['level']

            # Data by current employee from static_tree_page_view ( == vi )
            employee_vi = employee[2][0]

            # Get employee fields from static_tree_page_view.
            position_name_vi = employee_vi.position.position_name
            day_vi = employee_vi.date_employment
            salary_vi = employee_vi.salary
            first_name_vi = employee_vi.first_name
            last_name_vi = employee_vi.last_name

            # Date about the graph.
            employee_vi_graph = employee[2][1]
            open_gd_vi = employee_vi_graph['open']
            close_gd_vi = employee_vi_graph['close']
            level_gd_vi = employee_vi_graph['level']

            # Check that the position name from datasource and view are the same.
            self.assertEqual(position_name_ds, position_name_vi)

            # Check that the day (date_employment)  from datasource and view are the same.
            self.assertEqual(day_ds, day_vi)

            # Check that the salary from datasource and view are the same.
            self.assertEqual(salary_ds, salary_vi)

            # Check that the first_name from datasource and view are the same.
            self.assertEqual(first_name_ds, first_name_vi)

            # Check that the last_name from datasource and view are the same.
            self.assertEqual(last_name_ds, last_name_vi)

            # Check that the open( field for graph ) from datasource and view are the same.
            self.assertEqual(open_gd_ds, open_gd_vi)

            # Check that the close( field for graph ) from datasource and view are the same.
            self.assertEqual(close_gd_ds, close_gd_vi)

            # Check that the level( field for graph ) from datasource and view are the same.
            self.assertEqual(level_gd_vi, level_gd_ds)