from django.urls import path

from . import views

app_name = 'contacts2'
urlpatterns = [
    path('', views.ContactListView.as_view(), name='index'),
    path('create/', views.create_view, name='create'),
    path('<int:contact_id>/', views.edit_view, name='edit'),
]
