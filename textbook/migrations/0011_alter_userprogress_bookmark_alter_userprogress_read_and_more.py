# Generated by Django 5.0.6 on 2024-11-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0010_alter_userprogress_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='understood',
            field=models.BooleanField(default=False),
        ),
    ]
