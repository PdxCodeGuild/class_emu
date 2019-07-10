
from django.urls import path

from . import views

app_name = 'ajax_demo'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_demo_data/', views.save_demo_data, name='save_demo_data')
]
