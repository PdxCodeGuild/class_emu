from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book, Author

def index(request):
    books = Book.objects.order_by('author', 'title')
    books_sortby_title = Book.objects.filter(checked_out=False).order_by('title')
    context = {'books': books, 'books_sortby_title': books_sortby_title}
    return render(request, 'library/index.html', context)

def checkout(request):
    book_title = request.POST['checkout_select']
    book = Book.objects.get(title=book_title)
    book.checked_out = True
    book.save()
    # return HttpResponse('ok')
    return HttpResponseRedirect(reverse('library:index'))
