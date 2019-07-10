from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TodoAjaxItem

import json

def index(request):
    return render(request, 'todoajax/index.html')




def get_todos(request):

    # data = {
    #     'todos': [{
    #         'text': 'walk the dog'
    #     },{
    #         'text': 'butter the cat'
    #     }]
    # }

    data = {'todos': []}
    todo_items = TodoAjaxItem.objects.all()
    for todo_item in todo_items:
        data['todos'].append({
            'text': todo_item.text
        })
        #data['todos'].append(todo_item) #Object of type 'TodoAjaxItem' is not JSON serializable
    # print(data)
    return JsonResponse(data)


def save_todo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoAjaxItem(text=todo_text)
    todo_item.save()
    return HttpResponse('ok')
