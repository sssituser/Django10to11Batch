from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def home(request):
    Emplist = Employee.objects.all()
    empdict ={"employees":Emplist}
    return render(request,'myapp/home.html',empdict)