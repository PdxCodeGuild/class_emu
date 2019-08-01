from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import ShortURL
import random

# Create your views here.

def index(request):
    shorturls = ShortURL.objects.all()
    context = {
        'shorturls': shorturls
    }
    return render(request, 'shortenerapp/index.html', context)
    
def saveurl(request):
    lurl = request.POST['long_url']

    # generate code
    password_Length = 6
    int_Counter = 0
    random_choice = 'abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''
    while int_Counter < password_Length:
        password += random.choice(random_choice)
        int_Counter += 1
    print(password)
    newshorturl = ShortURL(longurl = lurl, code = password)
    newshorturl.save()
    return HttpResponseRedirect(reverse('ShortenerApp:index'))

def code_redirect(request, code):
    
    a_url = ShortURL.objects.get(code=code)
    # find the record in the ShortURL table whose code matches the given code (.get)
    # redirect to the url associated with that code (redirect)
    return redirect(a_url.longurl)