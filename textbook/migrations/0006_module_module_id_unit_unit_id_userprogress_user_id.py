# Generated by Django 5.0.6 on 2024-07-08 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0005_unit_featured_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='module_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_id',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userprogress',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_user_progress', to=settings.AUTH_USER_MODEL),
        ),
    ]
