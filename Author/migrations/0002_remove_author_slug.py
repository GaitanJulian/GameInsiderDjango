# Generated by Django 4.1.6 on 2023-02-15 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]
