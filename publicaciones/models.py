from django.db import models
from django.contrib.auth.models import User
from juegos.models import Game
from Author.models import Author
from tinymce.models import HTMLField
from django_resized import ResizedImageField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    thumbnail = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True)

    def __str__(self):
        return self.title