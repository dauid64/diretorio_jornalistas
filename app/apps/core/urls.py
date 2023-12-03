from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'contato/',
        views.ContatoView.as_view(),
        name='contato'
    ),
    path(
        'sobre/',
        views.SobreView.as_view(),
        name='sobre'
    )
]
