# GAME INSIDER
#### Video Demo:  <URL HERE>
#### Description: The following project is a page to publish forums about video games, users can search for posts about their favorite videos, like and comment on the posts they want. Users can also edit their own profile, and log in to see in an orderly fashion all the posts they have made. The project was made using the django framework.

## Models
Let's start by reviewing all the models created.


### Author
The author models refers to every user in the webpage, the model includes data as for example their full name or their profile picture.

### Game
This model refers to a Game that is possible to create a post about.

### Post, Like, Comment
This models refers to a publication that a user can make, i also created some other models to save the users likes and commentaries.


## Templates
Nos lets review some of the templates that we have for rendering the page.

### Registration

#### Bio.html
This html is rendered when a user wants to update any old information about himself.

#### Signin.html
An html that is rendered when a user wants to sign in to the webpage with an already created account

#### Signup.html
Similar to the previous one, this html is rendered when a user wants to create a new account.

#### Update.html
This html is pretty similar to the Bio.html and maybe i could only have one, but i decided to have theese two, this html is immediatily rendered after the user created a new account, in order to update the Author biography, their full name and the profile picture.

### Base.html
I should have started with this template, this is the base html for rendering all the other templates in the website, this html contains the navbar of the pages as well as some references for example to bootstrap. Every other template in the page inhherits from this template.

### Home.html
The Homepage of the website, counts with a centered search bar where users can search any post or content in the website. Just below the searchbar there is one carousel of popular games that users can find posts about

### Search.html
This is the html that is rendered when a user search any keyword, it display in columns of three post available.

### post_detail.html
This is the html that is rendered when a user clicks on a post to open it completely, it shows the thumbnail of the post as well as every important information. Here users can like the posts or make their own comments.

### create_post.html
This renders a form that allows the user to create a new publication.

### add_comment.html
This is a small form that is loaded inside the post_detail.html, this is the form that allows user to publicate any new comment.

## Views.py
Every Django project needs views to render the different pages of the website. I Created a few views to render specific functionalities of the website

### Author views.py
```
@login_required
def profile(request):
    context = {}
    author = Author.objects.get(user = request.user)
    posts = Post.objects.filter(author=author)
    context.update(
        {"posts" : posts,}
    )
    return render(request, 'profile.html', context)

```
This view renders the profile.html page with the necesary information. As you can see, it selects the author that matches the current user, then gather all the posts that were made by that author and send that information in the context dictionary.
```
def home(request):
    games = Game.objects.all()
    game_groups = [games[i:i+3] for i in range(0, len(games), 3)]
    context = {
        'game_groups': game_groups,
    }

    return render(request, 'home.html', context)
```
This view is in charge of rendering the homepage, it sends all the games registered in the database so they can be displayed in the carousel.

### Register views.py
```
def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("update_profile")
    context.update( {
        "form":form,
        "title" : "Signup",
    })
    return render(request, "registration/signup.html", context)

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  
    context.update({
        "form": form,
        "tittle": "Signin"
    })
    return render(request, "registration/signin.html", context)

@login_required
def update_profile(request):
    context = {}
    user = request.user
    form = UpdateForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit = False)
            update_profile.user = user
            update_profile.save()
            return redirect("home")

    context.update({
        "form" : form,
        "title" : "Update Profile"
    })
    return render(request, "registration/update.html", context)

@login_required
def update_bio(request):
    context = {}
    user = request.user
    author = get_object_or_404(Author, user=user)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=author)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    context.update({
        "form" : form,
        "title" : "Update Profile"
    })
    return render(request, "registration/bio.html", context)

@login_required
def logout(request):
    lt(request)
    return redirect("home")
```
All of the views here are methods related to the user management, for example, log in, log out, sign in.

### Posts views.py
```
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

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and comment.author.user == request.user:
        comment.delete()
    return redirect('post_detail', post_id=comment.post.id)
```
This methods are all related to the posts, for example here are the codes necesary for making a comment in a posts or deleting a comment. Searching posts, opening a post or liking a post.

## STATIC FILES
The static files include the css for all the project, I mainly used bootstrap but there was necessary to make custom styling to the page, also this static folder includes the logos used in the webpage as well as some images.