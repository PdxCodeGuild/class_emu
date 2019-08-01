from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'ShortenerApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('<str:code>/', views.code_redirect, name='code_redirect')
]