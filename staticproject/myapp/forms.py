from django import forms
from myapp.models import Employee
class EmployeeForm(forms.ModelForm):
    eid = forms.IntegerField()
    ename = forms.CharField(max_length=30)
    esal = forms.IntegerField()     
    class Meta:
        model = Employee
        fields='__all__'
