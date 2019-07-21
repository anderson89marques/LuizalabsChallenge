from luizalabs_challenge.employee_manager.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'phone', 'department', 'created_at']