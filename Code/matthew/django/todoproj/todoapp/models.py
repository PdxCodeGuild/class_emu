from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    type = models.ForeignKey('TodoItemType', null=True, blank=True, on_delete=models.SET_NULL, related_name='items')
    urgency = models.ForeignKey('TodoItemUrgency', on_delete=models.PROTECT, related_name='items')
    date_completed = models.DateTimeField(null=True, blank=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def completed(self):
        return self.date_completed != None
    
    def __str__(self):
        return self.text + ' ' + self.type.name + ' ' + self.urgency.name

class TodoItemType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + ' ' + str(self.items.count())
    
class TodoItemUrgency(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + ' ' + str(self.items.count())