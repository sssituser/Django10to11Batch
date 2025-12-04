from django.shortcuts import render

# Create your views here.
def home(request):

    employees = [
        {"eid":111,"ename":"kiran","esal":50000},
        {"eid":112,"ename":"MaheshBabu","esal":70000},
        {"eid":113,"ename":"Jr.Ntr","esal":80000},
        {"eid":114,"ename":"Allu Arjun","esal":55000},
        {"eid":115,"ename":"Pooja Hegde ","esal":50000},
        {"eid":116,"ename":"Samantha","esal":60000},
    ]
    empdict = {"emps":employees}
    return render(request,'myapp/home.html',empdict)