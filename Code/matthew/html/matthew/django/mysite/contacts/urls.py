from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('<int:contact_id>/save/', views.save_contact, name='save_contact'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
    path('create/', views.create_contact, name='create_contact'),
    path('save_new_contact/', views.save_new_contact, name='save_new_contact'),
]
