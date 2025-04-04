from django import forms
from .models import Employee, Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'location']

class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'gender', 
                 'date_of_birth', 'hire_date', 'salary', 'department', 
                 'address', 'is_active']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }