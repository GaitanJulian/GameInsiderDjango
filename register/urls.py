from django.urls import path

from . import views
from .views import signup, signin, update_profile, logout, update_bio

urlpatterns = [
    #ruta, vista, nombre interno
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path("update_profile/", update_profile, name="update_profile"),
    path('logout/', logout, name='logout'),
    path("update_bio/", update_bio, name="update_bio")
    ]