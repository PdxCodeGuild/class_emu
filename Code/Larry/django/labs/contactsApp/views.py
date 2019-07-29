from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse

from .models import Contact

def index(request):
    contacts_list = Contact.objects.order_by('id')
    context = {'contacts_list': contacts_list}
    return render(request, 'contactsApp/index.html', context)


def detail(request, contact_id):
    # use the id to look up a contacts (Contact.objects.get)
    # pass that contact to a template to be rendered
    # return HttpResponse(contact_id)
    contact_details = Contact.objects.filter(id=contact_id)
    context = {'contact_details': contact_details}
    return render(request, 'contactsApp/details.html', context)
