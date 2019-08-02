from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # links app (urls.py) to view (views.py) - second part of path - http://127.0.0.1:8000/todoapp/index/
    path('addtodo/', views.addtodo)
]
