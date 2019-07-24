from django.db import models




class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    # text = models.TextField() # (effectively) unlimited length
    completed = models.BooleanField()
    
    def __str__(self):
        return self.text


    


