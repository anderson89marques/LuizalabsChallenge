from luizalabs_challenge.employee_manager.models import Employee
from luizalabs_challenge.employee_manager.serializers import EmployeeSerializer
from rest_framework import generics


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer