from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from Author.models import Author
from .models import Post
# Create your views here.

@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            return redirect("home")

    context.update({
    "form": form,
    "title" : "Create New Post"
   })
    return render(request, "create_post.html", context) 


def search_post(request):
    context = {}
    query = request.GET.get('search')
    posts = Post.objects.filter(title_icontains=query)
    context.update({
        "posts" : posts,
    })
    return render(request, 'search.html', context)