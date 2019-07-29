from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField('birthday')
    phone_number = models.CharField(max_length=200)
    is_cell = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
# Create your models here.
