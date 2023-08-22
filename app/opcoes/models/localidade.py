from django.db import models


class Estados(models.Model):
    descricao = models.CharField(max_length=64)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return '{}'.format(self.descricao)


class Cidades(models.Model):
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.descricao)


class Pais(models.Model):
    descricao = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.descricao)
