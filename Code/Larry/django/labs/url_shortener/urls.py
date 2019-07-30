from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
    # /url_shortener/
    path('', views.index, name='index'),
    # /short/abc123/
    path('<str:code>/', views.redirect, name='redirect'),
]
