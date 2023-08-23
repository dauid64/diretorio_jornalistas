from django.db import models
from opcoes.models import VeiculoDeComunicacao, TipoDePublicacao
from obras.models import ObraJornalistica


class Publicao(models.Model):
    veiculo_de_comunicacao = models.ForeignKey(VeiculoDeComunicacao, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(TipoDePublicacao, on_delete=models.DO_NOTHING)
    data = models.DateField()
    link = models.URLField(max_length=254, blank=True, null=True)
    anexo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True, null=True)
    obra_jornalistica = models.ForeignKey(ObraJornalistica, models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.obra_jornalistica)
