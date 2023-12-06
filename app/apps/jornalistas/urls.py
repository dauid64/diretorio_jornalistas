from django.urls import path
from . import views


app_name = 'jornalistas'


urlpatterns = [
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
    ),
    path(
        'diploma/<int:pk>',
        views.DownloadDiploma.as_view(),
        name='download_diploma'
    ),
    path(
        'curriculo/<int:pk>',
        views.DownloadCurriculo.as_view(),
        name='download_curriculo'
    )
]
