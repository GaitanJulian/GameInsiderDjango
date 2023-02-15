from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from Author.models import Author
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
# Create your views here.
@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None, request.FILES)
    if request.method == "POST":
         if form.is_valid(): 
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.author = author
            new_post.save()
            return redirect("home") 
    context.update({
    "form": form,
    "title" : "Create New Post"
   })
    return render(request, "create_post.html", context) 


def search(request):
    context = {}
    query = request.GET.get('search')
    posts = Post.objects.filter(title__contains=query)
    context.update({
        "posts" : posts,
        "query" : query,
    })
    return render(request, 'search.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})