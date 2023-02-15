from django.shortcuts import render
from .models import FeaturedPost
from publicaciones.models import Post 
from juegos.models import Game
from Author.models import Author
# Create your views here.

def home(request):
    games = Game.objects.all()
    game_groups = [games[i:i+3] for i in range(0, len(games), 3)]
    context = {
        'game_groups': game_groups,
    }

    return render(request, 'home.html', context)