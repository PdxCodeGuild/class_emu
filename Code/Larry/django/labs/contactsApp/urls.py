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
    # /contactsApp/123/edit
    path('<int:contact_id>/edit/', views.edit, name='edit'),
    # /contactsApp/save
    path('save_contact/', views.save_contact, name='save_contact'),
    # /contactsApp/123/delete
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
