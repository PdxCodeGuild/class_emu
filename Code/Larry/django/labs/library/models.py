from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField()

    def __str__(self):
        return self.author.name + ': ' + self.title
