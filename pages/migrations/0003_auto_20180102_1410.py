# Generated by Django 2.0 on 2018-01-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_mainentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioentity',
            name='bio_title',
            field=models.CharField(help_text="Cover letter must have a title 'coverletter', and entries title must start with a word'list'", max_length=50),
        ),
        migrations.AlterField(
            model_name='mainentity',
            name='main_title',
            field=models.CharField(help_text='DO NOT MODIFY PRE-DEFINED TITLES.', max_length=50),
        ),
    ]
