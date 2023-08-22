from django.db import models


class TipoDeVeiculo(models.Model):
    descricao = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.descricao)

class VeiculoDeComunicacao(models.Model):
    nome = models.CharField(max_length=254)
    tipo_de_veiculo = models.ForeignKey(TipoDeVeiculo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.nome)


