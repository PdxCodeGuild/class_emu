
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_todos/', views.get_todos, name='get_todos'),
]