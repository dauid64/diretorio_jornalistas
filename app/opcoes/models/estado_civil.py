from django.db import models

class EstadoCivil(models.Model):
    descricao = models.CharField(max_length=64)

    def __str__(self):
        return '{}'.format(self.descricao)
