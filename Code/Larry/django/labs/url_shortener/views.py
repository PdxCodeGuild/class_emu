from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import shortURLgen
import string
import random

def index(request):
    shortened_urls = shortURLgen.objects.order_by('-id')
    context = {'shortened_urls': shortened_urls}
    return render(request, 'url_shortener/index.html', context)

def saveurl(request):
    # get the characters to choose from from string()
    letters = string.ascii_letters      # UPPER and lower case letters, a-Z
    digits = str(string.digits)         # integers, 0-9
    letters_digits = letters + digits   # combine letters & digits into one string
    counter = 0
    shorturl_code = ''
    while counter < 5:
        shorturl_code += random.choice(letters_digits)
        counter = counter + 1
    # Print the 5-character code
    # return HttpResponse(your_password)
    long_url = request.POST['long_url']
    short_url = shortURLgen(code=shorturl_code, long_url=long_url)
    short_url.save()
    return HttpResponseRedirect(reverse('url_shortener:index'))

def redir_to_long_url(request, code):
    url_object = shortURLgen.objects.get(code=code)
    print(url_object.long_url)
    return redirect(url_object.long_url)
