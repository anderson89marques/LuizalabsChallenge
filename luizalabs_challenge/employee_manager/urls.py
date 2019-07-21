from luizalabs_challenge.employee_manager.views import EmployeeListView, EmployeeDetailView

from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee-list'), 
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]