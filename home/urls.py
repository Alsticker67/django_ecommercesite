from django.contrib import admin
from django.urls import path
from home import views
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path('first',views.first,name="first"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('familypack',views.familypack,name="familypack")
    
    
 
]