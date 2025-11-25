from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('login/',views.login),

]