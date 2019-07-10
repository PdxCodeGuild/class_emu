from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import GalleryItem

def index(request):
    gallery_items = GalleryItem.objects.all()
    context = {
        'gallery_items': gallery_items
    }
    return render(request, 'fileapp/index.html', context)



def save_gallery_item(request):
    title = request.POST['title']
    image = request.FILES['image']
    gallery_item = GalleryItem(title=title, image=image)
    gallery_item.save()
    return HttpResponseRedirect(reverse('fileapp:index'))
