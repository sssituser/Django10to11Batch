from django import forms
from myapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'EId': forms.NumberInput(attrs={'placeholder': 'Enter Employee ID'}),
            'EName': forms.TextInput(attrs={'placeholder': 'Enter Employee Name'}),
            'ESal': forms.NumberInput(attrs={'placeholder': 'Enter Salary'}),
        }
        error_messages = {
            'EId': {
                'required': "Employee ID is required"
            },
            'EName': {
                'required': "Employee Name cannot be empty"
            },
            'ESal': {
                'required': "Please enter salary amount"
            }
        }
