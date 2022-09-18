from datetime import datetime
from decimal import Decimal

from django.test import TestCase
from django.db.models import ProtectedError
from app.models import Positions, Employees


class PositionsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Create object for Position and Employees models.
        ( Create position and employee ).
        """

        # Create position.
        position_name = 'Ведущий специалист'
        position = Positions.objects.create(position_name=position_name)

        # Create position without employee.
        position_name_without = 'Должность без сотрудника'
        position_without = Positions.objects.create(position_name=position_name_without)

        print('Positions {0} creation completed successfully'.format(position_name))
        # Save id and name of created position in self.employee_id and self.position_name.
        cls.position_id = position.id
        cls.position_name = position.position_name

        # At the same for position without employee.
        cls.position_without_id = position_without.id
        cls.position_without_name = position_without.position_name

        # Create fields for employee for this position.
        day = datetime.strptime('01/09/22', '%m/%d/%y').date()
        salary = Decimal('20000.23')
        first_name = 'Иван'
        last_name = 'Иванов'

        # Let's create a employee:
        employee = Employees.add_root(first_name=first_name,
                                      last_name=last_name,
                                      position=position,
                                      date_employment=day,
                                      salary=salary)
        employee.refresh_from_db()

        # Save id of created employee in self.employee_id.
        cls.employee_id = employee.id

        print('Employee {0} {1} creation completed successfully'.format(first_name, last_name))

    def test_positions_verbose_name(self):
        """
        This test check verbose_name for position_name field.
        """

        # Get object from database.
        position = Positions.objects.get(position_name='Ведущий специалист')
        # Get verbose_name from object.
        position_name = position._meta.get_field('position_name').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(position_name, 'Должность')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(position_name, ' Должность')

    def test_position_name_max_length(self):
        """
        This test check that the position_name field have maximum len == 30.
        """
        position = Positions.objects.get(position_name='Ведущий специалист')
        max_length = position._meta.get_field('position_name').max_length
        # Check left borderline case.
        self.assertNotEqual(max_length, 29)
        # Check for the true value.
        self.assertEqual(max_length, 30)
        # Check right borderline case.
        self.assertNotEqual(max_length, 31)

    def test_position_name_str_method(self):
        """
        This test check that str method return position_name.
        """

        # Get object from database.
        position = Positions.objects.get(position_name='Ведущий специалист')
        # Compare method str result with position_name ( they must be equals ).
        self.assertEquals(position.position_name, str(position))

    def test_employees_verbose_name(self):
        """
        This test check verbose_name for all fields Employees model.
        """

        # Get object from database.
        employee = Employees.objects.get(id=self.employee_id)

        # Get verbose_name from object for different fields.

        # For position_name
        first_name = employee._meta.get_field('first_name').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(first_name, 'Имя')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(first_name, ' Имя')

        # For last_name
        last_name = employee._meta.get_field('last_name').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(last_name, 'Фамилия')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(last_name, ' Фамилия')

        # For position
        position = employee._meta.get_field('position').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(position, 'Должность')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(position, ' Должность')

        # For date_employment
        date_employment = employee._meta.get_field('date_employment').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(date_employment, 'Дата трудоустройства')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(date_employment, ' Дата трудоустройства')

        # For date_employment
        salary = employee._meta.get_field('salary').verbose_name
        # Compare verbose_name with the correct one.
        self.assertEquals(salary, 'Зарплата')
        # Compare verbose_name with the incorrect one.
        self.assertNotEquals(salary, ' Зарплата')

    def test_employees_max_length(self):
        """
        This test check that the all fields Employees model have maximum len == 30.
        """

        # Get object from database.
        employee = Employees.objects.get(id=self.employee_id)

        # Get max_length from object for different fields.

        # For first_name
        max_length = employee._meta.get_field('first_name').max_length
        # Check left borderline case.
        self.assertNotEqual(max_length, 29)
        # Check for the true value.
        self.assertEqual(max_length, 30)
        # Check right borderline case.
        self.assertNotEqual(max_length, 31)

        # For last_name
        max_length = employee._meta.get_field('last_name').max_length
        # Check left borderline case.
        self.assertNotEqual(max_length, 29)
        # Check for the true value.
        self.assertEqual(max_length, 30)
        # Check right borderline case.
        self.assertNotEqual(max_length, 31)

    def test_employees_foreign_key(self):
        """
        This test check foreign key in Employees model.
        """

        # Get object from database.
        employee = Employees.objects.get(id=self.employee_id)
        # Get position_id this object ( from Employees table )
        position_id_employees = employee.position_id

        # Compare position this object between two tables Employees and Position
        self.assertEquals(position_id_employees, self.position_id)

    def test_employees_foreign_key_delete_protect(self):
        """
        This test check that deleting positions is protected.
        """

        # Get object from database.
        position = Positions.objects.filter(id=self.position_id)
        position_without = Positions.objects.filter(id=self.position_without_id)

        # Deleting the position should be impossible, let's check it:
        with self.assertRaises(ProtectedError):
            # Let's run the deletion which should cause a raise.
            position.delete()

        # But deletion position_without should be possible, let's check it:
        position_without.delete()

    def test_decimal_field(self):
        """
        This test check decimal field in salary ( field in Employees model ).
        """

        # Get object from database.
        employee = Employees.objects.get(id=self.employee_id)

        # Get max_digits and decimal_places from object for different fields.
        max_digits = employee._meta.get_field('salary').max_digits
        decimal_places = employee._meta.get_field('salary').decimal_places

        # Check left borderline case.
        self.assertNotEqual(max_digits, 9)
        # Compare max_digits with the correct one.
        self.assertEquals(max_digits, 10)
        # Check right borderline case.
        self.assertNotEqual(max_digits, 11)

        # Check left borderline case.
        self.assertNotEqual(decimal_places, 1)
        # Compare decimal_places with the correct one.
        self.assertEquals(decimal_places, 2)
        # Check right borderline case.
        self.assertNotEqual(decimal_places, 3)

    def test_employees_str_method(self):
        """
        This test check that str method return correct string for Employees model.
        """

        # Get object from database.
        employee = Employees.objects.get(id=self.employee_id)
        # Create correct string:
        correct_str = '{0} {1}'.format(employee.first_name, employee.last_name)
        # Check method str:
        self.assertEquals(correct_str, str(employee))
