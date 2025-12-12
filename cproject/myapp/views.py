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


from django.shortcuts import get_object_or_404
from myapp.models import Employee

def view(request,id):
    emp = get_object_or_404(Employee,id=id)
    return render(request,'myapp/show.html',{'emp':emp})

def edit(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        empRec = EmployeeForm(request.POST, instance=emp)
        if empRec.is_valid():
            empRec.save()
            return redirect('abc')   # 👈 return is required

    # GET request → show existing data
    form = EmployeeForm(instance=emp)
    return render(request, 'myapp/edit.html', {'form': form})







