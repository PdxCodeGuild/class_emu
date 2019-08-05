from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import json

from django.contrib.auth.decorators import login_required

from .models import TodoItem

@login_required
def index(request):
    return render(request, 'todoapp/index.html', {})


# be careful not to allow users to access other user's data
@login_required
def detail(request, todoitem_id):
    # todo_item = TodoItem.objects.get(id=todoitem_id)
    # if todo_item.user.id != request.user.id:
    #     raise Http404("Don't try to access another user's data")
    # todo_item = request.user.todo_items.get(id=todoitem_id)
    todo_item = TodoItem.objects.filter(id=todoitem_id, user_id=request.user.id)
    if todo_item.exists():
        todo_item = todo_item.first()
    else:
        raise Http404("Don't try to access another user's data")

    return render(request, 'todoapp/detail.html', {'todo_item': todo_item})

@login_required
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
    for todo_item in request.user.todo_items.all():
        data['todos'].append(todo_item.text) # JSON can only contain objects, arrays, strings, numbers, and booleans
    
    return JsonResponse(data)

@login_required
def save_todo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoItem(text=todo_text, user=request.user)
    todo_item.save()
    return HttpResponse('ok')
    # return HttpResponseRedirect(reverse('todoapp:get_todos'))
