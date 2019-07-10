
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('view2/', views.view2, name='view2'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
]
