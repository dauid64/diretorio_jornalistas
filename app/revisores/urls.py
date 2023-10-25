from django.urls import path
from . import views

app_name = "revisores"

urlpatterns = [
    path(
        'analise/jornalistas',
        views.RevisorAnaliseView.as_view(),
        name='analise_jornalistas'
    ),
    path(
        'analise/jornalistas/aprovar/<int:id>',
        views.RevisorAprovarView.as_view(),
        name='aprovar'
    ),
    path(
        'analise/jornalistas/reprovar/<int:id>',
        views.RevisorReprovarView.as_view(),
        name='reprovar'
    ),
    path(
        'analise/jornalistas/perfil/<int:id>',
        views.RevisorAnalisePerfilView.as_view(),
        name='analise_jornalista_perfil'
    )
]
