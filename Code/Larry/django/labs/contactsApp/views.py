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
    contact = Contact.objects.get(id=contact_id)
    context = {'contact': contact}
    return render(request, 'contactsApp/detail.html', context)

def create(request):
    # return HttpResponse("Create new contact")todo_text = request.POST['todo_text']
    return render(request, 'contactsApp/create.html')

def create_contact(request):
    print(request.POST)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    is_cell = 'is_cell' in request.POST

    contact = Contact(first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, is_cell=is_cell)
    contact.save()
    # return HttpResponse('Create new contact')
    return HttpResponseRedirect(reverse('contactsApp:index'))

def edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {'contact': contact}
    # return HttpResponse("Edit existing contact")
    return render(request, 'contactsApp/edit.html', context)

def save_contact(request):
    contact = Contact.objects.get(id=request.POST['id'])
    contact.id = request.POST['id']
    contact.first_name = request.POST['first_name']
    contact.last_name = request.POST['last_name']
    contact.birthday = request.POST['birthday']
    contact.phone_number = request.POST['phone_number']
    contact.is_cell = 'is_cell' in request.POST

    # contact = Contact(id=id, first_name=first_name, last_name=last_name, birthday=birthday, phone_number=phone_number, is_cell=is_cell)
    contact.save()
    # return HttpResponse('Save existing contact')
    return HttpResponseRedirect(reverse('contactsApp:detail', args=(contact.id,)))
