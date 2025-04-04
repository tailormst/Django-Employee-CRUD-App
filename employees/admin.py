from django.contrib import admin
from .models import Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'department', 'hire_date', 'is_active')
    list_filter = ('department', 'is_active', 'hire_date', 'gender')
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'hire_date'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)