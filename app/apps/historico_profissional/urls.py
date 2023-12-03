from django.urls import path
from . import views


app_name = 'experiencia'


urlpatterns = [
    path(
        'cadastro/',
        views.CadastroHistoricoView.as_view(),
        name='cadastro'
    )
]