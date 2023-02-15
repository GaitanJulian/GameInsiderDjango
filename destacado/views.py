from django.shortcuts import render
from .models import FeaturedPost
from publicaciones.models import Post 
from juegos.models import Game
# Create your views here.

def home(request):
    featured_posts = FeaturedPost.objects.all()
    featured_games = Game.objects.all()
    posts = Post.objects.all()
    context = {
        'featured_post' : featured_posts,
        'posts' : posts,
        'featured_games': featured_games,
    }

    return render(request, 'home.html', context)