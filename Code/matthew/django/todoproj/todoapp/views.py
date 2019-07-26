from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import TodoItem, TodoItemType, TodoItemUrgency

def index(request):
    context = {
        'items': TodoItem.objects.filter(date_completed__isnull=True),
        'completed_items': TodoItem.objects.filter(date_completed__isnull=False),
        'types': TodoItemType.objects.order_by('name'),
        'urgencies': TodoItemUrgency.objects.all()
    }
    return render(request, 'todoapp/index.html', context)


def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_type_id = request.POST['todo_type_id']
    todo_urgency_id = request.POST['todo_urgency_id']
    
    
    todo_type = None
    if todo_type_id != '':
        todo_type = TodoItemType.objects.get(id=todo_type_id)
    
    todo_urgency = TodoItemUrgency.objects.get(id=todo_urgency_id)
    
    todo_item = TodoItem(text=todo_text, type=todo_type, urgency=todo_urgency, date_completed=None)
    todo_item.save()
    
    return HttpResponseRedirect(reverse('todoapp:index'))


def completetodo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))