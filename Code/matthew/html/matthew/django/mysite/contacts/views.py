from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Contact, Gender, EyeColor

def index(request):
    contacts = Contact.objects.order_by('name')
    context = {
        'contacts': contacts,
        'num_contacts': len(contacts),
    }
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    genders = Gender.objects.order_by('name')
    eye_colors = []
    for eye_color in EyeColor.objects.order_by('name'):
        eye_colors.append({
            'id': eye_color.id,
            'name': eye_color.name,
            'checked': eye_color in contact.eye_colors.all()
        })
    context = {
        'contact': contact,
        'genders': genders,
        'eye_colors': eye_colors,
    }
    return render(request, 'contacts/detail.html', context)



def save_contact(request, contact_id):
    print(request.POST)
    # print(request.POST.getlist('eye_color_id'))
    contact = Contact.objects.get(pk=contact_id)
    contact.name = request.POST['contact_name']
    contact.age = request.POST['contact_age']

    # gender = Gender.objects.get(pk=request.POST['contact_gender_id'])
    # contact.gender = gender
    contact.gender_id = request.POST['contact_gender_id']
    contact.eye_colors.clear()

    for eye_color in EyeColor.objects.all():
        if f'eye_color_{eye_color.id}' in request.POST: # checkbox is checked
            contact.eye_colors.add(eye_color)

    # fruits = {'apples': 1, 'bananas': 2, 'pears': 3}
    # if 'apples' in fruits:
    #     print('we have apples.')

    contact.hot_or_not = 'contact_hot_or_not' in request.POST
    contact.phone_number = request.POST['contact_phone_number']
    contact.address = request.POST['contact_address']
    contact.save()


    return HttpResponseRedirect(reverse('contacts:index'))


def delete_contact(request, contact_id):
    # contact = Contact.objects.get(pk=request.POST['contact_id'])
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts:index'))

def create_contact(request):
    genders = Gender.objects.order_by('name')
    eye_colors = EyeColor.objects.order_by('name')
    context = {
        'genders': genders,
        'eye_colors': eye_colors
    }
    return render(request, 'contacts/create.html', context)



def save_new_contact(request):
    print(request.POST)

    contact_name = request.POST['contact_name']
    contact_age = request.POST['contact_age']
    contact_gender_id = request.POST['contact_gender_id']
    contact_hot_or_not = 'contact_hot_or_not' in request.POST
    contact_phone_number = request.POST['contact_phone_number']
    contact_address = request.POST['contact_address']

    # gender = Gender.objects.get(pk=contact_gender_id)

    contact = Contact(name=contact_name,
                        age=contact_age,
                        gender_id=contact_gender_id,
                        hot_or_not=contact_hot_or_not,
                        phone_number=contact_phone_number,
                        address=contact_address)
    contact.save()

    for eye_color in EyeColor.objects.all():
        if f'eye_color_{eye_color.id}' in request.POST: # checkbox is checked
            contact.eye_colors.add(eye_color)

    return HttpResponseRedirect(reverse('contacts:index'))
