from django.contrib import admin

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'department', 'phone',)
    list_display = ('name', 'email', 'department', 'phone',)


admin.site.register(Employee, EmployeeAdmin)
