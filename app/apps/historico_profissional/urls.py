from django.urls import path
from . import views


app_name = 'experiencia'


urlpatterns = [
    path(
        'cadastro/',
        views.CadastroHistoricoView.as_view(),
        name='cadastro'
    ),
    path(
        'editar/<int:pk>',
        views.EditarHistoricoView.as_view(),
        name='editar'
    ),
    path(
        'deletar/',
        views.DeletarExperienciaView.as_view(),
        name='deletar'
    )
]