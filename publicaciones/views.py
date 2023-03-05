from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from Author.models import Author
from .models import Post, Like
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
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
    context = {}
    post = get_object_or_404(Post, id=post_id)
    context.update({
        "post": post,
        'like_count': post.num_likes,
    })
    return render(request, 'post_detail.html', context)

@login_required
@csrf_exempt
def like_post(request):
    post_id = request.POST.get('post_id')
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
            like, created = Like.objects.get_or_create(post=post, user=request.user)
            if not created:
                like.delete()
            return JsonResponse({'success': True, 'like_count': post.num_likes()})
        except Post.DoesNotExist:
            pass
    return JsonResponse({'success': False})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_comment = form.save(commit=False)
            new_comment.author = author
            new_comment.post = post
            new_comment.save()
            form = CommentForm()  # reset the form for a new comment
            return redirect('post_detail', post_id=post.id)  # redirect to post detail page
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'form': form,
    }
    
    return render(request, 'post_detail.html', context)