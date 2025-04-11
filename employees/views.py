from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.forms import modelform_factory
from .models import Employee, Department

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    ordering = ['last_name', 'first_name']

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = modelform_factory(Employee, exclude=[])
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

    def form_valid(self, form):
        messages.success(self.request, 'Employee created successfully!')
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = modelform_factory(Employee, exclude=[])
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee-list')

    def form_valid(self, form):
        messages.success(self.request, 'Employee updated successfully!')
        return super().form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Employee deleted successfully!')
        return super().delete(request, *args, **kwargs)

# Department Views
class DepartmentListView(ListView):
    model = Department
    template_name = 'employees/department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(CreateView):
    model = Department
    form_class = modelform_factory(Department, exclude=[])
    template_name = 'employees/department_form.html'
    success_url = reverse_lazy('department-list')

    def form_valid(self, form):
        messages.success(self.request, 'Department created successfully!')
        return super().form_valid(form)

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = modelform_factory(Department, exclude=[])
    template_name = 'employees/department_form.html'
    success_url = reverse_lazy('department-list')

    def form_valid(self, form):
        messages.success(self.request, 'Department updated successfully!')
        return super().form_valid(form)

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'employees/department_confirm_delete.html'
    success_url = reverse_lazy('department-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Department deleted successfully!')
        return super().delete(request, *args, **kwargs)
