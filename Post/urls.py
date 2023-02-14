from django.urls import path


from .views import create_post, search_post

urlpatterns = [
    path("create_post", create_post, name="create_post"),
    path('search/', search_post, name='search')
]