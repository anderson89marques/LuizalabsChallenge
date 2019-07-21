from luizalabs_challenge.employee_manager.views import EmployeeListView, EmployeeDetailView

from django.urls import include, path

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee-list'), 
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
]