from django.urls import path

from . import views

app_name = 'contactsApp'
urlpatterns = [
    # /contactsApp/
    path('', views.index, name='index'),
    # /contactsApp/123/
    path('<int:contact_id>/', views.detail, name='detail'),
    # /contactsApp/create/
    path('create/', views.create, name='create'),
    # /contactsApp/create_contact/
    path('create_contact/', views.create_contact, name='create_contact'),
    # /contacts/123/edit
    path('<int:contact_id>/edit/', views.edit, name='edit'),
    # /contacts/save
    path('save_contact/', views.save_contact, name='save_contact'),
]
