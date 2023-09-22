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
        'perfil/<int:id>',
        views.PerfilUserView.as_view(),
        name='perfil'
    )
]
