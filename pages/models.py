from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.
class WorkEntity(models.Model):
    work_title = models.CharField(max_length=50)
    work_content = RichTextUploadingField()
    work_date = models.DateTimeField(auto_now_add=True)

class BioEntity(models.Model):
    bio_title = models.CharField(max_length=50, help_text="Cover letter must have a title 'coverletter', and entries title must start with a word'list'")
    bio_content = RichTextField()
    bio_date = models.DateTimeField(auto_now_add=True)

class MainEntity(models.Model):
    main_title = models.CharField(max_length=50, help_text="DO NOT MODIFY PRE-DEFINED TITLES.")
    main_content = models.TextField()
    main_date = models.DateTimeField(auto_now_add=True)
