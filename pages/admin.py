from django.contrib import admin
from .models import WorkEntity, BioEntity, MainEntity

class WorkEntityAdmin(admin.ModelAdmin):
    list_display = ('work_title', 'work_date', )

class BioEntityAdmin(admin.ModelAdmin):
    list_display = ('bio_title', 'bio_date', )

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['bio_title',] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []

class MainEntityAdmin(admin.ModelAdmin):
    list_display = ('main_title', 'main_content', )

    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['main_title',] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []

admin.site.register(WorkEntity, WorkEntityAdmin)
admin.site.register(BioEntity, BioEntityAdmin)
admin.site.register(MainEntity, MainEntityAdmin)
