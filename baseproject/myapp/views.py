from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def login(request):
    return render(request,'myapp/Login.html')

def register(request):
    return render(request,'myapp/Register.html')

def about(request):
    return render(request,'myapp/About.html')

def Contact(request):
    return render(request,'myapp/Contact.html')
