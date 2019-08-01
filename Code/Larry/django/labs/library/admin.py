from django.contrib import admin

from .models import Author
from .models import Book
from .models import BookCheckout

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookCheckout)
