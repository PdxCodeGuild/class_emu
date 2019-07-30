from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import URL

def index(request):
    # return HttpResponse("url_shortener index")
    shortened_urls = URL.objects.order_by('id')
    context = {'shortened_urls': shortened_urls}
    return render(request, 'url_shortener/index.html', context)

def saveurl(request):
    return HttpResponse("saveurl")

def redirect(request, code):
    return HttpResponse("redirect to long_url" + ':' + code)
