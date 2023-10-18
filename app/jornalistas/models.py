from django.db import models
from django.db import models
from django.contrib.auth.models import User
from associacoes.models import Associacao
from opcoes.models import Cidades, Estados, Genero, EstadoCivil, VeiculoDeComunicacao
from smart_selects.db_fields import ChainedForeignKey
from obras.models import ObraJornalistica


class JornalistasManager(models.Manager):
    def aprovados(self):
        return self.filter(aprovado=True)


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_de_guerra = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    associacao = models.ForeignKey(Associacao,on_delete=models.DO_NOTHING)
    cpf = models.CharField(max_length=14)
    data_de_nascimento = models.DateField()
    telefone = models.CharField(max_length=50)
    estado = models.ForeignKey(Estados, on_delete=models.DO_NOTHING, blank=True, null=True)
    cidade = ChainedForeignKey(
        Cidades,
        chained_field='estado',
        chained_model_field='estado',
        show_all=False,
        auto_choose=False,
        sort=False,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.DO_NOTHING)
    foto = models.ImageField(null=True, blank=True)
    registro = models.CharField(max_length=50)
    diploma = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey('revisores.Revisor', on_delete=models.DO_NOTHING, null=True, blank=True)

    objects = JornalistasManager()

    def is_aprovado(self):
        if self.aprovado is True:
            return True
        return False

    def __str__(self):
        return '{}'.format(self.nome_de_guerra)


class HistoricoProfissional(models.Model):
    jornalista = models.ForeignKey(Jornalista, on_delete=models.CASCADE)
    veiculo_de_comunicacao = models.ForeignKey(VeiculoDeComunicacao , on_delete=models.DO_NOTHING)
    descricao = models.CharField(max_length=254)
    cargo = models.CharField(max_length=254)
    data_inicio = models.DateField()
    data_de_termino = models.DateField(blank=True, null=True)
    referencia = models.CharField(max_length=254)
    contato_da_referencia = models.CharField(max_length=254)

    def __str__(self):
        return '{} - {} - {}/{}'.format(self.veiculo_de_comunicacao, 
                                        self.cargo, 
                                        self.data_inicio, 
                                        self.data_de_termino)