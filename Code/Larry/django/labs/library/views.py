from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Author

def index(request):
    # return HttpResponse("Library: Hello world!")
    books = Book.objects.order_by('-id')
    context = {'books': books}
    return render(request, 'library/index.html', context)
