from django.contrib import admin
from .models import PhotoEntity

class PhotoEntityAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'photo_title', 'photo_date', )

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['photo_file',] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []

admin.site.register(PhotoEntity, PhotoEntityAdmin)
