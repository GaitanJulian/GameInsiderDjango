from django.shortcuts import render
from .models import FeaturedPost
# Create your views here.

def home(request):
    featured_posts = FeaturedPost.objects.all()
    context = {
        'featured_post' : featured_posts
    }

    return render(request, 'home.html', context)