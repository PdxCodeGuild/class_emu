from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import TodoItem

def index(request):
    return render(request, 'todoapp/index.html', {})

def get_todos(request):
    # data = {
    #     'contacts': [{
    #         'name': 'Joe',
    #         'age': 34
    #     },{
    #         'name': 'Jill',
    #         'age': 32
    #     }]
    # }
    
    data = {'todos':[]}
    for todo_item in TodoItem.objects.all():
        data['todos'].append(todo_item.text)
    
    return JsonResponse(data)


