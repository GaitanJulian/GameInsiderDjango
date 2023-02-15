from django import template
from Author.models import Author

register = template.Library()

@register.simple_tag
def author_profile_pic(user):
    try:
        author = Author.objects.get(user=user)
        if author.profile_pic:
            return author.profile_pic.url
    except Author.DoesNotExist:
        pass
    return None