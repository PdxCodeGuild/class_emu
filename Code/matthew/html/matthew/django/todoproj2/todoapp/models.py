from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_todo_items(self):
        return self.items.filter(date_completed__isnull=True)

    def get_completed_items(self):
        return self.items.filter(date_completed__isnull=False)

    def __str__(self):
        #items = self.items.all()
        return self.name


class TodoItem(models.Model):
    text = models.TextField()
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)


    def completed(self):
        return self.date_completed is not None

    def __str__(self):
        return self.list.name + ': ' + self.text



# | text         | completed | date_completed |
# | walk the dog | false     | 4/18/2019      | <- contradiction
# | walk the dog | true      | null           | <- contradiction
