from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='game_thumbnails/')
    developer = models.CharField(max_length=100)

    def __str__(self):
        return self.name