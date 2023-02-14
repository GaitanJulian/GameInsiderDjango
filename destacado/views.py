from django.shortcuts import render
from .models import FeaturedPost
from publicaciones.models import Post 
# Create your views here.

def home(request):
    featured_posts = FeaturedPost.objects.all()
    posts = Post.objects.all()
    context = {
        'featured_post' : featured_posts,
        'posts' : posts,
    }

    return render(request, 'home.html', context)