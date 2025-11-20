from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h2 style='text-align:center;color:red'>Hi Iam home function views.py </h2>")

def register(request):
    return HttpResponse("<h2 style='text-align:center;color:green' >Hi Iam register function from views.py</h2>")

def login(request):
    return HttpResponse("<h2 style='text-align:center;color:blue'>Hi Iam Login function from views.py</h2>")