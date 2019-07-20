from .models import Employee
from django.contrib import admin


class EmployeeAdmin(admin.ModelAdmin):
    #model = Employee
    #fields = ('name', 'email', 'department', 'phone',)
    list_display = ('name', 'email', 'department', 'phone',)

admin.site.register(Employee, EmployeeAdmin)