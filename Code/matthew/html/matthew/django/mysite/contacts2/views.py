from django.shortcuts import render, reverse
from django.views import generic
from contacts.models import Contact, Gender, EyeColor
from .forms import ContactForm
from django.http import HttpResponseRedirect


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contacts2/contact_list.html'


def create_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('contacts2:index'))
    else:
        form = ContactForm()
    return render(request, 'contacts2/create.html', {'form': form})


def edit_view(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        form.save()
    form = ContactForm(instance=contact)
    return render(request, 'contacts2/edit.html', {'form': form})
