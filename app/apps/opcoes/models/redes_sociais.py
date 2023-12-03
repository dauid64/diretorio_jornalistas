from django.db import models


class TipoDeRedeSocial(models.Model):
    descricao = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.descricao)


class RedesSociais(models.Model):
    jornalista = models.ForeignKey('jornalistas.Jornalista', on_delete=models.CASCADE)
    link = models.URLField(max_length=254)
    tipo_de_rede_social = models.ForeignKey(TipoDeRedeSocial, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.tipo_de_rede_social)
