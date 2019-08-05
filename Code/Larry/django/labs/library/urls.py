from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    # /library/
    path('', views.index, name='index'),
    # /library/checkout/
    path('checkout/', views.checkout, name='checkout'),
    # /library/v2/
    path('v2/', views.v2, name='v2'),
    # /library/checkout_v2/
    path('checkout_v2/', views.checkout_v2, name='checkout_v2'),
    # /library/checkin/
    path('checkin/', views.checkin, name='checkin'),
    # /library/v2/1/detail/
    path('v2/detail/<int:book_id>/', views.book_detail, name='book_detail'),
]
