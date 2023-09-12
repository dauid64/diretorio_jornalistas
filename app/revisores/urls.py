from django.urls import path
from . import views

app_name = "revisores"

urlpatterns = [
    path(
        'analise/jornalistas',
        views.RevisorAnaliseView.as_view(),
        name='analise'
    ),
    path(
        'analise/jornalistas/aprovar/<int:id>',
        views.RevisorAprovarView.as_view(),
        name='aprovar'
    )
]
