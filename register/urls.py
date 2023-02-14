from django.urls import path

from . import views
from .views import signup, signin, update_profile

urlpatterns = [
    #ruta, vista, nombre interno
    path('signup/', signup, name='singup'),
    path('signin/', signin, name='singin'),
    path('update_profile/', update_profile, name="update_profile"),
    ]