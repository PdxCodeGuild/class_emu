from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from .models import TodoList, TodoItem



# list views =================================================================

def index(request):

    # if request.method == 'POST':
    #     todo_list_name = request.POST['todo_list_name']
    #     todo_list = TodoList(name=todo_list_name)
    #     todo_list.save()

    todo_lists = TodoList.objects.order_by('date_created')
    context = {
        'todo_lists': todo_lists,
    }
    return render(request, 'todoapp/index.html', context)


def create_list(request):
    print(request.POST)
    todo_list_name = request.POST['todo_list_name']
    todo_list = TodoList(name=todo_list_name)
    todo_list.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def delete_list(request):
    print(request.POST)
    todo_list_id = request.POST['todo_list_id']
    todo_list = TodoList.objects.get(pk=todo_list_id)
    todo_list.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))


def delete_list2(request, todo_list_id):
    todo_list = TodoList.objects.get(pk=todo_list_id)
    todo_list.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))


def delete_list3(request):
    todo_list_id = request.GET['todo_list_id']
    todo_list = TodoList.objects.get(pk=todo_list_id)
    todo_list.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))




# item views =======================================================

def detail(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, pk=todo_list_id)
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todoapp/detail.html', context)

def create_todo_item(request):

    todo_list_id = request.POST['todo_list_id']
    todo_item_text = request.POST['todo_item_text']

    # todo_list = TodoList.objects.get(pk=todo_list_id)
    # todo_item = TodoItem(text=todo_item_text, list=todo_list)
    todo_item = TodoItem(text=todo_item_text, list_id=todo_list_id)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:detail', args=(todo_list_id,)))

def complete_todo_item(request, todo_item_id):
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    #return HttpResponseRedirect(reverse('todoapp:detail', args=(todo_item.list.id,)))
    return HttpResponseRedirect(reverse('todoapp:detail', kwargs={'todo_list_id':todo_item.list.id}))


def restore_todo_item(request, todo_item_id):
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.date_completed = None
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:detail', args=(todo_item.list.id,)))
