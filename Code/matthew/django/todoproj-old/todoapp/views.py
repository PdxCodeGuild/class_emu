from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem


def addtodo(request):
    # print(request.POST)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    return HttpResponseRedirect('/todoapp/index/')

def index(request):
    # for todo in TodoItem.objects.all():
    #     print(todo.text + ' ' + str(todo.completed))
    context = {
        'title': 'Todo List',
        'todos': TodoItem.objects.order_by('text')
    }
    return render(request, 'todoapp/index.html', context)
