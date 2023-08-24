from django.urls import path
from .views import RevisorAnaliseView

app_name = "revisores"

urlpatterns = [
    path(
        'analise',
        RevisorAnaliseView.as_view(),
        name='analise'
    )
]
