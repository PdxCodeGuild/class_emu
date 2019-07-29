from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def index(request):
    return HttpResponse('Index: ok')

def details(request, contacts_id):
    return HttpResponse('Details: ok' + ' ' + str(contacts_id))


def new_contact(request):
    return HttpResponse('New_Contact: ok')

def edit_contact(request, contacts_id):
    return HttpResponse('New_Edit: ok')
# Create your views here.
