
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', include('todoapp.urls')),
    path('todoajax/', include('todoajax.urls')),
]
