# Generated by Django 5.0.6 on 2024-07-07 13:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0004_rename_status_syllabus_module_status_module_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
