from django.db import models

import luizalabs_challenge.employee_manager.validators as validators 

class Employee(models.Model):
    name = models.CharField(max_length=100, validators=[validators.validate_name])
    email = models.EmailField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, validators=[validators.validate_phone_number])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name = "Employee"

    def __str__(self):
        return self.name