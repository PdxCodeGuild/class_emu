from django.db import models




class AjaxDemoData(models.Model):
    text = models.CharField(max_length=200)
    favorite_animal = models.CharField(max_length=200)
    hot_or_not = models.BooleanField()
    
