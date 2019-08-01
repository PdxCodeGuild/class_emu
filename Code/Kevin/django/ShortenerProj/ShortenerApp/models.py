from django.db import models

class ShortURL(models.Model):
    longurl = models.CharField(max_length=200)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code
# Create your models here.
