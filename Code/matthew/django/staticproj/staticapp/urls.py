
from django.urls import path

from . import views


urlpatterns = [
    path('page1/', views.page1),
    path('page2/', views.page2)
]