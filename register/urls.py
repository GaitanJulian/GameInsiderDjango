from django.urls import path

from . import views
from .views import signup, signin

urlpatterns = [
    #ruta, vista, nombre interno
    path('signup/', signup, name='singup'),
    path('signin/', signin, name='singin'),

]