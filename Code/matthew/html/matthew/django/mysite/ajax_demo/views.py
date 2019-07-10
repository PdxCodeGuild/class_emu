from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import AjaxDemoData

def index(request):
    return render(request, 'ajax_demo/index.html', {})

def save_demo_data(request):
    data = json.loads(request.body)
    text = data['text']
    favorite_animal = data['favorite_animal']
    hot_or_not = data['hot_or_not']
    ajax_demo_data = AjaxDemoData(text=text, favorite_animal=favorite_animal, hot_or_not=hot_or_not)
    ajax_demo_data.save()
    
    return HttpResponse('ok')
