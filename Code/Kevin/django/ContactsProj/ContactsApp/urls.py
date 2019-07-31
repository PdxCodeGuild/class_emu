from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'ContactsApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contacts_id>/', views.details, name='detail'),
    path('new/', views.new_contact, name='new_contact'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('<int:contacts_id>/edit/', views.edit_contact, name='edit'),
    path('<int:contacts_id>/edit/submit/', views.edit_submission, name='edit_submission')
]