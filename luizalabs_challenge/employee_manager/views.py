from luizalabs_challenge.employee_manager.models import Employee
from luizalabs_challenge.employee_manager.serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework import permissions


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]