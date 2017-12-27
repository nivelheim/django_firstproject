from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.html import mark_safe
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.signals import saved_file
from django.db.models.signals import post_save

# Create your models here.
class PhotoEntity(models.Model):
    photo_title = models.CharField(max_length=50)
    photo_file = models.ImageField(upload_to='images/', help_text="Files cannot exceed 1.5MB.")
    photo_date = models.DateTimeField(auto_now_add=True)

    def image_thumb(self):
        if self.photo_file:
            return mark_safe('<img src="%s.250x250_q85_crop.jpg" style="width: 100px; height: 100px;" />' % self.photo_file.url)

    image_thumb.short_description = 'Thumb'
    image_thumb.allow_tags = True


@receiver(post_delete, sender=PhotoEntity)
def remove_file_from_s3(sender, instance, using, **kwargs):
    #instance.photo_file.delete(save=False)
    thumbmanager = get_thumbnailer(instance.photo_file)
    thumbmanager.delete(save=False)

@receiver(post_save, sender=PhotoEntity)
def create_thumbs(sender, instance, using, **kwargs):
    options = {'size': (250, 250), 'crop': True}
    thumb_url = get_thumbnailer(instance.photo_file).get_thumbnail(options).url
