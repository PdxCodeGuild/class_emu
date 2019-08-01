from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Book, Author, BookCheckout

def index(request):
    books = Book.objects.order_by('author', 'publish_date')
    books_sortby_title = Book.objects.filter(checked_out=False).order_by('title')
    context = {'books': books, 'books_sortby_title': books_sortby_title}
    return render(request, 'library/index.html', context)

def v2(request):
    books = Book.objects.order_by('author', 'title')
    books_available = Book.objects.filter(checked_out=False).order_by('title')
    books_notavailable = Book.objects.filter(checked_out=True).order_by('title')
    # book_lendee = Book.objects.get(bookcheckout__book=books_notavailable)
    # print(book_lendee[0])
    context = {
        'books': books,
        'books_available': books_available,
        'books_notavailable': books_notavailable,
        # 'book_lendee': book_lendee,
    }
    return render(request, 'library/v2.html', context)

def checkout(request):
    book_title = request.POST['checkout_select']
    book = Book.objects.get(title=book_title)
    book.checked_out = True
    book.save()
    return HttpResponseRedirect(reverse('library:index'))

def checkout_v2(request):
    lendee = request.POST['lendee']
    book_title = request.POST['checkout_select']
    book = Book.objects.get(title=book_title)
    book.checked_out = True
    book.save()
    book_checkout_details = BookCheckout(name=lendee, book=book, checkout_date=timezone.now())
    book_checkout_details.save()
    return HttpResponseRedirect(reverse('library:v2'))

def checkin(request):
    book_title = request.POST['checkin_select']
    book = Book.objects.get(title=book_title)
    book.checked_out = False
    book.save()
    book_checkout_details = BookCheckout.objects.get(book_id=book.id).delete()
    return HttpResponseRedirect(reverse('library:v2'))

def book_detail(request, book_id):
    books_details = Book.objects.get(id=book_id)
    title = books_details.title
    author = books_details.author
    pub_date = books_details.publish_date
    desc = books_details.description
    desc_url = books_details.desc_url
    img_url = books_details.image_url
    context = {
        'title': title,
        'author': author,
        'pub_date': pub_date,
        'desc': desc,
        'desc_url': desc_url,
        'img_url': img_url,
    }
    return render(request, 'library/book_detail.html', context)
    # return HttpResponse('ok')
