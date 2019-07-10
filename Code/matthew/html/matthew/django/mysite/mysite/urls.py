
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('contacts/', include('contacts.urls')),
    path('contacts2/', include('contacts2.urls')),
    path('users/', include('users.urls')),
    path('fileapp/', include('fileapp.urls')),
    path('githubbrowser/', include('githubbrowser.urls')),
    path('ajax_demo/', include('ajax_demo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
