from django.db import models
from apps.jornalistas.models import Jornalista
from apps.opcoes.models import VeiculoDeComunicacao


class HistoricoProfissional(models.Model):
    jornalista = models.ForeignKey(Jornalista, on_delete=models.CASCADE)
    veiculo_de_comunicacao = models.ForeignKey(VeiculoDeComunicacao,
                                               on_delete=models.PROTECT)
    descricao = models.CharField(max_length=254)
    cargo = models.CharField(max_length=254)
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}/{}'.format(self.veiculo_de_comunicacao,
                                        self.cargo,
                                        self.data_inicio,
                                        self.data_termino)


class Referencia(models.Model):
    historico_profissional = models.ForeignKey(HistoricoProfissional, 
                                               on_delete=models.CASCADE)
    nome = models.CharField(max_length=254)
    contato = models.CharField(max_length=254)

    def __str__(self):
        return self.nome
