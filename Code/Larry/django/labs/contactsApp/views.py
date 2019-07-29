from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse

from .models import Contact

def index(request):
    contacts_list = Contact.objects.order_by('last_name')
    context = {'contacts_list': contacts_list}
    return render(request, 'contactsApp/index.html', context)
