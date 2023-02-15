from .models import Author

def author(request):
    author = None
    if request.user.is_authenticated:
        try:
            author = Author.objects.get(user=request.user)
        except Author.DoesNotExist:
            pass
    return {'author': author}