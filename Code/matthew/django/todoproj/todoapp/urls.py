
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('savetodo/', views.savetodo, name='savetodo'),
    path('completetodo/', views.completetodo, name='completetodo')
]