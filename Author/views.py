from django.shortcuts import render
from publicaciones.models import Post
from .models import Author
from django.views.generic.list import ListView
from django.db.models import Count
# Create your views here.
def profile(request):
    context = {}
    author = Author.objects.get(user = request.user)
    posts = Post.objects.filter(author=author)
    context.update(
        {"posts" : posts,}
    )
    return render(request, 'profile.html', context)

