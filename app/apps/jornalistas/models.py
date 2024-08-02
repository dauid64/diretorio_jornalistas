from django.db import models
from django.contrib.auth.models import User
from apps.revisores.models import Revisor
from apps.associacoes.models import Associacao
from apps.opcoes.models import Genero, EstadoCivil
from apps.opcoes.models import Estados, Cidades


class JornalistasManager(models.Manager):
    def aprovados(self):
        return self.filter(aprovado=True)


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    show_nome_de_guerra = models.BooleanField(blank=True, default=False)
    nome_de_guerra = models.CharField(max_length=50)
    show_nome = models.BooleanField(blank=True, default=False)
    nome = models.CharField(max_length=255)
    show_sobrenome = models.BooleanField(blank=True, default=False)
    sobrenome = models.CharField(max_length=255)
    show_associacoes = models.BooleanField(blank=True, default=False)
    associacoes = models.ManyToManyField(Associacao, blank=True)
    show_cpf = models.BooleanField(blank=True, default=False)
    cpf = models.CharField(max_length=11)
    show_data_de_nascimento = models.BooleanField(blank=True, default=False)
    data_de_nascimento = models.DateField()
    show_ddi = models.BooleanField(blank=True, default=False)
    ddi = models.CharField(max_length=4)
    show_telefone = models.BooleanField(blank=True, default=False)
    telefone = models.CharField(max_length=11)
    show_genero = models.BooleanField(blank=True, default=False)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    show_estado_civil = models.BooleanField(blank=True, default=False)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.PROTECT)
    show_foto = models.BooleanField(blank=True, default=False)
    foto = models.ImageField(null=True, blank=True)
    show_registro = models.BooleanField(blank=True, default=False)
    registro = models.CharField(max_length=50, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey(Revisor, on_delete=models.PROTECT, null=True, blank=True)
    curriculo = models.FileField(upload_to='curriculos/%Y/%m/%d/', blank=True, null=True)
    funcao = models.CharField(max_length=255, null=True, blank=True)
    show_funcao = models.BooleanField(blank=True,default=False)
    cidade = models.ForeignKey(Cidades, on_delete=models.SET_NULL,null=True, blank=True)
    estado = models.ForeignKey(Estados, on_delete=models.SET_NULL,null=True, blank=True)
    show_cidade = models.BooleanField(blank=True, default=False)
    show_estado = models.BooleanField(blank=True, default=False)
    minibio = models.TextField(blank=True, null=True)

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
    descricao = models.CharField(max_length=255, null=True, blank=True)
    arquivo = models.ImageField(upload_to='diplomas/%Y/%m/%d/', null=True, blank=True)
