from django.shortcuts import render
# Create your views here.
def home(request):
    dict={'name':'kirunkumar'}
    employees = [
        {"id": 101, "name": "Arun", "dept": "IT", "salary": 50000},
        {"id": 102, "name": "Kiran", "dept": "HR", "salary": 45000},
        {"id": 103, "name": "Ravi", "dept": "Finance", "salary": 55000},
    ]
    employeeDict={'emps':employees}
    return render(request,'home.html',employeeDict)