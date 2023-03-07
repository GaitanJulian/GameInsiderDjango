from django.urls import path

from .views import profile

urlpatterns = [
    #ruta, vista, nombre interno
    path('profile/', profile, name='profile'),
]