from django.forms import ModelForm
from .models import PhotoEntity


class PhotoEntityForm(ModelForm):
    class Meta:
        model = PhotoEntity
        fields = ['photo_file', ]
        