from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('about/',views.about,name='about'),
    path('contact/',views.Contact,name='contact'),
]