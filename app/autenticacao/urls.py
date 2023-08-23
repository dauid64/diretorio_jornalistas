from django.urls import path
from .views import RegisterUserView, LoginUserView


app_name = 'autenticacao'


urlpatterns = [
    path(
        'registrar',
        RegisterUserView.as_view(),
        name='registrar'
    ),
    path(
        'login',
        LoginUserView.as_view(),
        name='login'
    )
]