from django.db import models
from apps.opcoes.models import TipoDePublicacao
from apps.obras.models import ObraJornalistica


class Publicao(models.Model):
    veiculo_de_comunicacao = models.CharField(max_length=55)
    tipo = models.ForeignKey(TipoDePublicacao, on_delete=models.PROTECT)
    data = models.DateField()
    link = models.URLField(max_length=254, blank=True, null=True)
    anexo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True, null=True)
    obra_jornalistica = models.ForeignKey(ObraJornalistica, models.CASCADE)

    def __str__(self):
        return '{}'.format(self.obra_jornalistica)
