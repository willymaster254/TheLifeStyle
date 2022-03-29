from django.contrib import admin 
from django.urls import path
from .import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('massage/', views.massage, name='massage'),
    path('Customer/', views.Customer, name='Customer'),
    path('success/', views.success, name='sucess'),
    # path('CustomerList/', views.CustomerList, name='CustomerList'),

    
    ]