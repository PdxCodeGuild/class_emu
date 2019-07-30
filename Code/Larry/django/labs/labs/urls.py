from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactsApp/', include('contactsApp.urls')),
    path('short/', include('url_shortener.urls')),
]
