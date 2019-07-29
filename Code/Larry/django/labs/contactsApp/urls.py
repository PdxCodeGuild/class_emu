from django.urls import path

from . import views

app_name = 'contactsApp'
urlpatterns = [
    # /contactsApp/
    path('', views.index, name='index'),
    # /contactsApp/123/
    path('<int:contact_id>/', views.detail, name='detail')
]
