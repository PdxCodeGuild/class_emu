from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('You\'re at the index')

def detail(request, blogpost_id):
    return HttpResponse('You\'re at the detail of the blog post with id ' + str(blogpost_id))

def create(request):
    return HttpResponse('You\'re at the blog post creation page')

def edit(request, blogpost_id):
    return HttpResponse('You\'re at the edit page of the blog post with id ' + str(blogpost_id))
