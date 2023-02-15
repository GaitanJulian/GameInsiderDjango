from django.shortcuts import render
from .models import FeaturedPost
from publicaciones.models import Post 
from juegos.models import Game
# Create your views here.

def home(request):
    #featured_posts = FeaturedPost.objects.all()
    games = Game.objects.all()
    game_groups = [games[i:i+3] for i in range(0, len(games), 3)]
    #posts = Post.objects.all()
    context = {
        #'featured_post' : featured_posts,
        #'posts' : posts,
        'game_groups': game_groups,
    }

    return render(request, 'home.html', context)