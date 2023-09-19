from django.db import models


class Associacao(models.Model):
    nome_fantasia = models.CharField(max_length=254)
    razao_social = models.CharField(max_length=254)
    cnpj = models.BigIntegerField()
    telefone = models.CharField()
    email = models.EmailField(max_length=254)
    presidente = models.CharField(max_length=254)
    # rede_sociais = models.ForeignKey(RedesSociais, on_delete=models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome_fantasia)