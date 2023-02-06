from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('', views.home, name='home')
]