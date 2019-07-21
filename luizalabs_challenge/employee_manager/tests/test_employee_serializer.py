from django.core.exceptions import ValidationError
from django.test import TestCase

from luizalabs_challenge.employee_manager.models import Employee
from luizalabs_challenge.employee_manager.serializers import EmployeeSerializer


class EmployeeSerializerTest(TestCase):
    def test_has_fields(self):
        expected = ['url', 'name', 'email',
                    'phone', 'department', 'created_at']
        serializer = EmployeeSerializer()
        self.assertEqual(expected, list(serializer.fields))

    def test_is_valid(self):
        serializer = make_validated_serializer()
        self.assertFalse(serializer.errors)

    def test_incorrect_email(self):
        serializer = make_validated_serializer(email='andersonoanjo18@')
        self.assertIn('email', serializer.errors)

    def test_incorrect_name(self):
        serializer = make_validated_serializer(name='Anderson Marques89')
        self.assertIn('name', serializer.errors)

    def test_incorrect_phone_number(self):
        serializer = make_validated_serializer(phone='99274-5052')
        self.assertIn('phone', serializer.errors)


def create_employee_data(name='Anderson Marques', email='andersonoanjo18@hotmail.com',
                         department='payments',
                         phone='(11) 99274-5052'):
    return dict(name=name, email=email, department=department, phone=phone)


def make_validated_serializer(**kwargs):
    data = dict(name='Anderson Marques', email='andersonoanjo18@hotmail.com',
                department='payments', phone='(11) 99274-5052')
    data = dict(data, **kwargs)
    serializer = EmployeeSerializer(data=data)
    serializer.is_valid()

    return serializer
