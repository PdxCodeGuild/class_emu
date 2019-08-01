from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="add some detail")
    desc_url = models.CharField(default="add a description url", max_length=200)
    image_url = models.CharField(default="https://lar-mo.com/images/lazy_placeholder.gif", max_length=200)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField()

    def __str__(self):
        return self.author.name + ': ' + self.title

class BookCheckout(models.Model):
    name = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(default=None, blank=True, null=True)
    checkin_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name + ': ' + self.book.title
