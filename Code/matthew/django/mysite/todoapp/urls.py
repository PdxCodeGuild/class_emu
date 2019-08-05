
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_todos/', views.get_todos, name='get_todos'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('detail/<int:todoitem_id>/', views.detail, name='detail'),
]