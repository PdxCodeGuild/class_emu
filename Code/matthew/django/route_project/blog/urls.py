from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # /blog/
    path('', views.index, name='index'),
    # /blog/5/, /blog/123/
    path('<int:blogpost_id>/', views.detail, name='detail'),
    # /blog/create/
    path('create/', views.create, name='create'),
    # /blog/5/edit
    path('<int:blogpost_id>/edit/', views.edit, name='edit'),
]
