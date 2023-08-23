from django.urls import path
from .views import LoginUserView


app_name = 'autenticacao'


urlpatterns = [
    path(
        'login',
        LoginUserView.as_view(),
        name='registrar'
    )
]
