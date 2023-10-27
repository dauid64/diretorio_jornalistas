from django.urls import path
from . import views


app_name = 'jornalistas'


urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'cadastro',
        views.CadastroJornalistaView.as_view(),
        name='cadastrar'
    ),
    path(
        'perfil/<int:pk>',
        views.PerfilJornalistaView.as_view(),
        name='perfil'
    ),
    path(
        'editar-perfil/<int:pk>',
        views.EditarJornalistaView.as_view(),
        name='editar'
    )
]
