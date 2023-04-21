# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('SignupPage/', views.SignupPage,name='SignupPage'),
    path('LoginPage/', views.LoginPage,name='LoginPage'),
    path('home', views.home,name='home'),
]
