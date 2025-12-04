from django.shortcuts import render
from myapp.forms import EmployeeForm
# Create your views here.
def home(request):
    form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Employee Added Successfully...")
    return render(request,'myapp/home.html',{'empForm':form})