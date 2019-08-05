from django.db import models

class shortened_url(models.Model):
    code = models.CharField(max_length=200, unique=True)
    long_url = models.CharField(max_length=200)

    def __str__(self):
        return self.code + ': ' + self.long_url
