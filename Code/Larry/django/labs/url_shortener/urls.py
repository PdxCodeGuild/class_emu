from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
    # /short/
    path('', views.index, name='index'),
    # /short/saveurl
    path('saveurl/', views.saveurl, name='saveurl'),
    # /short/abc123/
    path('<str:code>/', views.redir_to_long_url, name='redir_to_long_url'),
]
