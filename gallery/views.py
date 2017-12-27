from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import PhotoEntity


def upload(request):
    entities = PhotoEntity.objects.order_by('-photo_date')
    return render(request, 'gallery/photoentity_form.html', {'entities': entities})

def page(request, page_id):
    entities = PhotoEntity.objects.order_by('-photo_date')
    paginator = Paginator(entities, 12) # Show 25 contacts per page

    pages = paginator.get_page(page_id)
    return render(request, 'gallery/photoentity_form.html', {'pages': pages})
