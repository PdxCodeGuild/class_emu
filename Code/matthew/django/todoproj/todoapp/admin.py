from django.contrib import admin

from .models import TodoItem, TodoItemType, TodoItemUrgency

admin.site.register(TodoItem)
admin.site.register(TodoItemType)
admin.site.register(TodoItemUrgency)