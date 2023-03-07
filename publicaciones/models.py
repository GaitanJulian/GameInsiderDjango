from django.db import models
from django.contrib.auth.models import User
from juegos.models import Game
from Author.models import Author
from tinymce.models import HTMLField
from django_resized import ResizedImageField
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    thumbnail = ResizedImageField(size=[480, 360], quality=100, upload_to="authors", default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def num_likes(self):
        return self.like_set.count()

    def num_comments(self):
        return self.comments.count()

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)