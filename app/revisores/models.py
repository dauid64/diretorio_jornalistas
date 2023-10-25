from django.db import models
from django.contrib.auth.models import User
from jornalistas.models import Jornalista
from associacoes.models import Associacao


class Revisor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    associacao = models.ForeignKey(Associacao, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.usuario, self.associacao)