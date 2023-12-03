from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView


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
    )
]