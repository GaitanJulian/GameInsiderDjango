from django.urls import path


from .views import create_post, search, post_detail, like_post, add_comment, delete_comment

urlpatterns = [
    path("create_post", create_post, name="create_post"),
    path('search/', search, name='search'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('like_post/', like_post, name='like_post'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]