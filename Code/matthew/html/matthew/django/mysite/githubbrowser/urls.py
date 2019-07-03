

from django.urls import path
from . import views

app_name = 'githubbrowser'
urlpatterns = [
    path('', views.index, name='index')
]
