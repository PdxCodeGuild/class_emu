from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # /users/login/
    path('login/', views.login, name='login'),
    # /users/register/
    path('register/', views.register, name='register'),
    # /users/logout/
    path('logout/', views.logout, name='logout'),
]
