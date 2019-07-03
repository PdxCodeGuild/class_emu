from django.contrib import admin

from .models import Contact, Gender, EyeColor

admin.site.register(Contact)
admin.site.register(Gender)
admin.site.register(EyeColor)
