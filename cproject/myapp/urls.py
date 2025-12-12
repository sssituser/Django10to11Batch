from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('employees/',views.employees, name='abc'),
    
    path('view/<int:id>/',views.view, name='view'),
    path('edit/<int:id>/',views.edit, name='edit'),
    
]