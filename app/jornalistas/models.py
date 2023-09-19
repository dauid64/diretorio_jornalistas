from django.db import models
from django.db import models
from django.contrib.auth.models import User
from associacoes.models import Associacao
from revisores.models import Revisor
from opcoes.models import Cidades, Estados, Genero, EstadoCivil, VeiculoDeComunicacao
from obras.models import ObraJornalistica


class HistoricoProfissional(models.Model):
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


class Jornalista(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_de_guerra = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    associacao = models.ForeignKey(Associacao,on_delete=models.DO_NOTHING)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    telefone = models.CharField(max_length=50)
    estado = models.ForeignKey(Estados, on_delete=models.DO_NOTHING,null=True, blank = True)
    cidade = models.ForeignKey(Cidades, on_delete=models.DO_NOTHING,null=True, blank = True)
    genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING, null=True, blank = True)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.DO_NOTHING,null=True, blank = True)
    foto = models.ImageField(null=True, blank=True)
    registro = models.CharField(max_length=50, null=True, blank=True)
    diploma = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    revisor_responsavel = models.ForeignKey(Revisor,on_delete=models.DO_NOTHING, null=True)
    obras_jornalisticas = models.ManyToManyField(ObraJornalistica)
    historico_profissional = models.ManyToManyField(HistoricoProfissional)

    def __str__(self):
        return '{}'.format(self.nome_de_guerra)

