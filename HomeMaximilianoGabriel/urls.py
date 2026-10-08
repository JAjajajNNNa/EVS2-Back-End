from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('accion/', views.genero_accion, name='accion'),
    path('scifi/', views.genero_scifi, name='scifi'),
]