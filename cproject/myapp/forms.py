from django import forms
from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
    eid = forms.IntegerField(label='Emp ID')
    ename = forms.CharField(max_length=30,label='Name')
    esal = forms.IntegerField(label='Salary')
    class Meta:
        model = Employee
        fields ='__all__'