from django.urls import path

from . import views

urlpatterns = [
    # /contactsApp/
    path('', views.index, name='index'),
    # /contactsApp/123/
    path('<int:contact_id>/', views.detail)
]
