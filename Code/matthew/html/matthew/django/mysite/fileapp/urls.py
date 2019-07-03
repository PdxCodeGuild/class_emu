
from django.urls import path

from . import views

app_name = 'fileapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_gallery_item/', views.save_gallery_item, name='save_gallery_item'),
]
