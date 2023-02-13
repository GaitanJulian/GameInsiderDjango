# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from tinymce.models import HTMLField

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400)
    bio = HTMLField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True)
    
    def __str__(self):
        return self.fullname
    