from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from django.urls import reverse 

def index(request):
    contacts_list = Contact.objects.order_by('last_name')[:10]
    context = {
        'current_contact_list': contacts_list,
        'message': 'hello world!'
    }
    return render(request, 'contactsapp/index.html', context)

def details(request, contacts_id):
    contact = get_object_or_404(Contact, pk=contacts_id)
    context = {
        'contact': contact,
        'message': 'Hello world!'
    }
    return render(request, 'contactsapp/detail.html', context)


def new_contact(request):
    
    return render(request, 'contactsapp/new.html')


def create_contact(request):
    #print(request.POST)
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    birthday = request.POST['birthday']
    p_number = request.POST['phone_number']
    cell = 'is_cell' in request.POST

    a_contact = Contact(first_name=f_name, last_name=l_name, birthday=birthday, phone_number=p_number, is_cell=cell)
    a_contact.save()

    # get the data out of the dictionary request.POST['first_name']
    # create a Contact record and save it
    # redirect back to the index page HttpResponseRedirect
    # return HttpResponseRedirect(reverse('ContactsApp:results', args=(question.id,)))
    return HttpResponseRedirect(reverse('ContactsApp:index'))


def edit_contact(request, contacts_id):
    contact = get_object_or_404(Contact, pk=contacts_id)
    context = {
        'contact': contact
    }
    return render(request, 'contactsapp/edit.html', context)
# Create your views here.

def edit_submission(request, contacts_id):
    print(request.POST)
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    birthday = request.POST['birthday']
    p_number = request.POST['phone_number']
    cell = 'is_cell' in request.POST

    current_contact = Contact.objects.get(id=contacts_id)
    current_contact.first_name=f_name
    current_contact.last_name=l_name 
    current_contact.birthday=birthday 
    current_contact.phone_number=p_number 
    current_contact.is_cell=cell
    current_contact.save()
    return HttpResponseRedirect(reverse('ContactsApp:detail', args=(contacts_id,)))