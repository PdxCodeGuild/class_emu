

from django.urls import path
from . import views

app_name = 'todoajax'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_todos/', views.get_todos, name='get_todos'),
    path('save_todo/', views.save_todo, name='save_todo'),
]
