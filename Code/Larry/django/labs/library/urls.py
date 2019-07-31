from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    # /library/
    path('', views.index, name='index'),
    # /library/checkout/
    path('checkout/', views.checkout, name='checkout')
]
