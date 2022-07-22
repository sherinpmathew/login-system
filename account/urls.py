from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('student/', views.student, name='student'),
    path('staff/', views.staff, name='staff'),
    path('editor/', views.editor, name='editor'),
]