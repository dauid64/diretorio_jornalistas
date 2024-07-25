from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, RecuperarSenha


app_name = 'autenticacao'


urlpatterns = [
    path(
        'login',
        LoginUserView.as_view(),
        name='login'
    ),
    path(
        'logout',
        LogoutUserView.as_view(),
        name='logout'
    ),
    path(
        'recuperar_senha',
        RecuperarSenha.as_view(),
        name='recuperar_senha'
    ),
]