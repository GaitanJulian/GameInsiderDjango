from django.shortcuts import render
from publicaciones.models import Post
from .models import Author
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile(request):
    context = {}
    author = Author.objects.get(user = request.user)
    posts = Post.objects.filter(author=author)
    context.update(
        {"posts" : posts,}
    )
    return render(request, 'profile.html', context)

