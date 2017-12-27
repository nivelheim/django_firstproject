from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import WorkEntity, BioEntity, MainEntity
from gallery.models import PhotoEntity
from .forms import ContactForm

# Create your views here.
def workView(request):
    works = WorkEntity.objects.all()
    return render(request, 'pages/works.html', {'works': works})

def bioView(request):
    lists = BioEntity.objects.filter(bio_title__startswith='list')
    coverletter = None
    try:
        coverletter = BioEntity.objects.get(bio_title='coverletter')
    except ObjectDoesNotExist:
        coverletter = None
    return render(request, 'pages/biography.html', {'lists': lists, 'coverletter': coverletter})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['contact_email']
            title = form.cleaned_data['contact_title']
            content = form.cleaned_data['contact_content']
            try:
                send_mail(title, content, email, ['Sung.Jo@hotmail.com'])
                data = {
                    'response': 'Email was sent.'
                }
            except BadHeaderError:
                data = {
                    'response': 'There was a problem sending an email.'
                }
                return JsonResponse(data)
            return JsonResponse(data)
    return render(request, "pages/contact.html", {'form': form})

def indexView(request):
    photos = PhotoEntity.objects.order_by('-photo_date')[:4]
    try:
        headertone = MainEntity.objects.get(main_title='main_header_title1')
        headerttwo = MainEntity.objects.get(main_title='main_header_title2')
        headercone = MainEntity.objects.get(main_title='main_header_content1')
        headerctwo = MainEntity.objects.get(main_title='main_header_content2')
        contentp = MainEntity.objects.get(main_title='main_content_p')
    except MainEntity.DoesNotExist:
         raise Http404("Some entries have invalid title name. Please check.")
    context = {
        'images': photos,
        'headertone': headertone,
        'headerttwo': headerttwo,
        'headercone': headercone,
        'headerctwo': headerctwo,
        'contentp': contentp
    }
    return render(request, 'pages/index.html', context)
