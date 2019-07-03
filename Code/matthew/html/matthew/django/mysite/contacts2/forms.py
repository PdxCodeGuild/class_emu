from django.forms import ModelForm
from contacts.models import Contact, Gender, EyeColor

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = []
