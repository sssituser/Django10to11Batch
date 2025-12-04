from django.shortcuts import render

# Create your views here. 
def home(request):
    return render(request,'myapp/home.html')

def register(request):
    return render(request,'myapp/register.html')

def login(request):
    return render(request,'myapp/login.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def users(request):
    return render(request,'myapp/userlist.html')