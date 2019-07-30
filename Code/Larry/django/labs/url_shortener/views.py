from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import URL

def index(request):
    shortened_urls = URL.objects.order_by('id')
    context = {'shortened_urls': shortened_urls}
    return render(request, 'url_shortener/index.html', context)

def saveurl(request):
    return HttpResponse("saveurl")

def redir_to_long_url(request, code):
    url_object = URL.objects.get(code=code)
    print(url_object.long_url)
    return redirect(url_object.long_url)
