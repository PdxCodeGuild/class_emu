from django.db import models

class URL(models.Model):
    code = models.CharField(max_length=200)
    long_url = models.CharField(max_length=200)

    def __str__(self):
        return self.code
