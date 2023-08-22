from django.db import models

class ObraJornalistica(models.Model):
    titulo = models.CharField(max_length=254)
    descricao = models.CharField(max_length=254)

    def __str__(self):
        return '{}'.format(self.titulo)
