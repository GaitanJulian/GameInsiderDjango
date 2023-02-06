from django.db import models
from publicaciones.models import Post 
# Create your models here.
class FeaturedPost(models.Model):
    image = models.ImageField(upload_to='featured/')
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    active = models.BooleanField(default=False) # Para indicar si la publicacion hace parte del carrusel
    order = models.PositiveSmallIntegerField() # Para ordenar las publicaciones

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title