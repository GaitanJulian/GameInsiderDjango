# Generated by Django 4.1.6 on 2023-02-15 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_post_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]