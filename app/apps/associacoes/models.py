from django.db import models


class Associacao(models.Model):
    nome_fantasia = models.CharField(max_length=254, blank=True, null=True)
    razao_social = models.CharField(max_length=254, blank=True, null=True)
    cnpj = models.BigIntegerField( blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254 , blank=True, null=True)
    presidente = models.CharField(max_length=254, blank=True, null=True)
    # rede_sociais = models.ForeignKey(RedesSociais, on_delete=models.DO_NOTHING)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.nome_fantasia)