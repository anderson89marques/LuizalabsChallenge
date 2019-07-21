from rest_framework import serializers

from luizalabs_challenge.employee_manager.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'phone', 'department', 'created_at']
