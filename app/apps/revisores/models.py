from django.db import models
from django.contrib.auth.models import User
from apps.associacoes.models import Associacao


class Revisor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    associacoes = models.ManyToManyField(Associacao, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.username