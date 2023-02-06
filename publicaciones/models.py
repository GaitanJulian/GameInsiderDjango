from django.db import models
from django.contrib.auth.models import User
from juegos.models import Game

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post_thumbnail')

    def __str__(self):
        return self.title