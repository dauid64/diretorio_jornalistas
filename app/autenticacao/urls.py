from django.urls import path
from .views import LoginUserView


app_name = 'autenticacao'


urlpatterns = [
    path(
        'registrar',
        LoginUserView.as_view(),
        name='registrar'
    )
]
