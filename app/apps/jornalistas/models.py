from django.db import models
from django.contrib.auth.models import User
from apps.revisores.models import Revisor
from apps.associacoes.models import Associacao
from apps.opcoes.models import Genero, EstadoCivil


class JornalistasManager(models.Manager):
    def aprovados(self):
        return self.filter(aprovado=True)


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_de_guerra = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    associacoes = models.ManyToManyField(Associacao, blank=True)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    ddi = models.CharField(max_length=4)
    telefone = models.CharField(max_length=11)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT)
    foto = models.ImageField(null=True, blank=True)
    registro = models.CharField(max_length=50, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey(Revisor, on_delete=models.PROTECT, null=True, blank=True)

    objects = JornalistasManager()

    @property
    def is_aprovado(self):
        if self.aprovado is True:
            return True
        return False

    @property
    def is_want_revisor(self):
        if self.usuario.revisor:
            return True
        return False

    def __str__(self):
        return '{}'.format(self.nome_de_guerra)


class Diploma(models.Model):
    jornalista = models.ForeignKey(Jornalista, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    arquivo = models.ImageField(upload_to='diplomas/%Y/%m/%d/')
