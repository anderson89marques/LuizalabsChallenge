from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from luizalabs_challenge.employee_manager.models import Employee


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.obj = Employee(
            name='Anderson Marques',
            email='andersonoanjo18@hotmail.com',
            department='payments',
            phone='(11) 99274-5052',
        )
        self.obj.save()
    
    def test_create(self):
        self.assertTrue(Employee.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual("Anderson Marques", str(self.obj))
    
    def test_correct_email(self):
        self.assertTrue(self.obj.email, 'andersonoanjo18@hotmail.com')
    
    def test_incorrect_email(self):
        self.obj.email = 'andersonoanjo18@'
        self.assertRaises(ValidationError, self.obj.save())
    
    def test_incorrect_name(self):
        self.obj.name = 'Anderson Marques89'
        self.assertRaises(ValidationError, self.obj.save())
    
    def test_incorrect_phone_number(self):
        self.obj.phone = '99274-5052'
        self.assertRaises(ValidationError, self.obj.save())


