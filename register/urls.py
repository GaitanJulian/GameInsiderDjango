from django.urls import path

from . import views
from .views import signup

urlpatterns = [
    #ruta, vista, nombre interno
    path('signup/', signup, name='singup')
]