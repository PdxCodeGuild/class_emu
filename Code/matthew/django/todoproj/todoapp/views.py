from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Fruits',
        'fruits': ['apples', 'bananas', 'pears']
    }
    return render(request, 'todoapp/index.html', context)