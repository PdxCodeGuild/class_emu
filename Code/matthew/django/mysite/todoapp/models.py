from django.db import models

from django.contrib.auth.models import User

class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_items')
    
    def __str__(self):
        return self.text
    
