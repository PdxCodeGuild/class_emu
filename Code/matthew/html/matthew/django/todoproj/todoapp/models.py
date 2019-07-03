from django.db import models
from django.utils import timezone

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    completed = models.BooleanField()
    # date_created = models.DateTimeField(auto_now_add=True)
    # date_edited = models.DateTimeField(auto_add=True)

    def __str__(self):
        return self.text
