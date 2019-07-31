from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import shortened_url
import string
import random

def index(request):
    shortened_urls = shortened_url.objects.order_by('-id')
    context = {'shortened_urls': shortened_urls}
    return render(request, 'url_shortener/index.html', context)

def saveurl(request):
    # get the characters to choose from from string()
    letters = string.ascii_letters      # UPPER and lower case letters, a-Z
    digits = str(string.digits)         # integers, 0-9
    letters_digits = letters + digits   # combine letters & digits into one string
    long_url = request.POST['long_url']

    while True:
        shorturl_code = ''
        for i in range(5):
            shorturl_code += random.choice(letters_digits)
        exist_count = shortened_url.objects.filter(code=shorturl_code).count()
        if exist_count >= 1:
            print("shorturl_code already exists")
        else:
            short_url = shortened_url(code=shorturl_code, long_url=long_url)
            short_url.save()
            break
    return HttpResponseRedirect(reverse('url_shortener:index'))

def redir_to_long_url(request, code):
    url_object = shortened_url.objects.get(code=code)
    print(url_object.long_url)
    return redirect(url_object.long_url)
