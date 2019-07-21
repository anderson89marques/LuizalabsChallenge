import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError

from luizalabs_challenge.employee_manager.models import Employee


class EmployeeNewPostValidTest(APITestCase):
    def setUp(self):
        self.url = reverse('employee-list')
        self.data = create_employee_data()
        self.response = self.client.post(self.url, self.data)

    def test_create_employee_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_create_employee(self):
        self.assertEqual(Employee.objects.count(), 1)
    

class EmployeeNewPostInvalidTest(APITestCase):
    def setUp(self):
        self.url = reverse('employee-list')

    def test_create_employee_invalid_post_status_code(self):
        data = create_employee_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_employee(self):
        self.assertEqual(Employee.objects.count(), 0)

    def test_create_employee_invalid_post_incorrect_name(self):
        data = create_employee_data(name='Anderson Marques1')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {'name': ['Name should not contains digit.']})
    
    def test_create_employee_invalid_post_incorrect_email(self):
        data = create_employee_data(email='andersonoanjo18')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {'email': ['Enter a valid email address.']})
    
    def test_create_employee_invalid_post_incorrect_phone(self):
        """
        Ensure phone number must have the right format '(XX) XXXXX-XXXX'
        """
        data = create_employee_data(phone='(11) 992745052')
        response = self.client.post(self.url, data)
        self.assertEqual(json.loads(response.content), {'phone': ["Phone number must have this format '(xx) xxxxx-xxxx'."]})


class EmployeeListTest(APITestCase):
    def setUp(self):
        self.url = reverse('employee-list')

    def test_get_employees_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_employees_with_empty_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data['results'], [])

    def test_get_employees(self):
        data = create_employee_data()
        employee = Employee.objects.create(**data)
        response = self.client.get(self.url)
        self.assertDictContainsSubset(data, json.loads(response.content)['results'][0])


class EmployeeDeleteTest(APITestCase):
    def setUp(self):
        data = create_employee_data()
        employee = Employee.objects.create(**data)
        self.url = reverse('employee-detail', kwargs={'pk':employee.pk})

    def test_delete_employee(self):
        response = self.client.delete(self.url)
        self.assertEqual(Employee.objects.count(), 0)


def create_employee_data(name='Anderson Marques', email='andersonoanjo18@hotmail.com',
                         department='payments',
                         phone='(11) 99274-5052'):
    return dict(name=name,email=email,department=department,phone=phone)