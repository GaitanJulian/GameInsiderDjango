# Generated by Django 4.1.6 on 2023-02-06 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='featured/')),
                ('title', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.post')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
