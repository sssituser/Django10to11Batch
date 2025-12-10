from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')


def register(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('abc')
    return render(request,'myapp/register.html',{'form':form})

def login(request):
    return render(request,'myapp/login.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')


from myapp.models import Employee

def employees(request):
    empList = Employee.objects.all()
    return render(request,'myapp/employees.html',{'empList':empList})







