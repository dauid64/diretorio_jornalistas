from django.urls import path
from . import views


app_name = 'associacoes'


urlpatterns = [
    path(
        'cadastro',
        views.CadastroAssociacoesView.as_view(),
        name='cadastro'
    )
]
