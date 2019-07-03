from django.db import models



class Gender(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EyeColor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, related_name='contacts')
    eye_colors = models.ManyToManyField(EyeColor)
    hot_or_not = models.BooleanField()
    phone_number = models.CharField(max_length=200)
    address = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    # {{contact.age_in_goats}}
    # def age_in_goats(self):
    #     return '🐐' * self.age



    def __str__(self):
        return self.name
