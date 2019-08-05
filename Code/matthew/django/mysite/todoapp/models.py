from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self):
        return self.text
    
