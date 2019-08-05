from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

def addtodo(request):
    # print(request.POST)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text, completed=False)
    todo_item.save()
    # print(todo_text)
    # return HttpResponse('ok')
    return HttpResponseRedirect('/todoapp/index/')

def index(request):
    # print("error") # this is output when you refresh the page, http://127.0.0.1:8000/todoapp/index/
    # return HttpResponse('ok')
    context = {
        'title': 'Todo List',
        'todos': TodoItem.objects.all()
    }
    return render(request, 'todoapp/index.html', context)
