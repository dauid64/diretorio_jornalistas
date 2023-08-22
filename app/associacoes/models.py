from django.db import models
from opcoes.models import RedesSociais


class Associacao(models.Model):
    nome_fantasia = models.CharField(max_length=254)
    razao_social = models.CharField(max_length=254)
    cnpj = models.IntegerField()
    ddd_telefone = models.CharField(max_length=2)
    telefone = models.CharField(max_length=9)
    email = models.EmailField(max_length=254)
    presidente = models.CharField(max_length=254)
    # rede_sociais = models.ForeignKey(RedesSociais, on_delete=models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome_fantasia)