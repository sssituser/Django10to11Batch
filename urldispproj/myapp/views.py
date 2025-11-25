from django.shortcuts import render,HttpResponse    

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hi Iam Home function from myapp</h1>")

def register(request):
    return HttpResponse("<h1>Hi Iam Register function from myapp</h1>")
def login(request):
    return HttpResponse("<h1>Hi Iam Login function from myapp</h1>")
