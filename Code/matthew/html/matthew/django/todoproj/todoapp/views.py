from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoItem

from django.utils import timezone

import random


def index(request):
    # html = '<html><head></head><body>'
    # html += '<ul>'
    # for i in range(10):
    #     html += '<li>' + str(i) + '</li>'
    # html += '</ul>'
    # html += '</body></html>'
    # return HttpResponse(html)

    # div = '<div>'
    # for i in range(100):
    #     div += str(random.randint(1,10)) + ','
    # div += '</div>'

    context = {
        'message': 'Todo List',
        'todos': TodoItem.objects.filter(completed=False),
        'completed_todos': TodoItem.objects.filter(completed=True)
    }

    return render(request, 'todoapp/index.html', context)


def view2(request):
    return HttpResponse('You\'re at view2')


def save_todo(request):
    # print(request.POST)
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text,
                        date_created=timezone.now(),
                        completed=False)
    todo_item.save()
    # return HttpResponse('ok')
    return HttpResponseRedirect(reverse('todoapp:index'))


def complete_todo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
