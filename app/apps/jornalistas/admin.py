from django.contrib import admin
from .models import Jornalista, Diploma


@admin.register(Jornalista)
class JornalistaAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'usuario', 'nome_de_guerra', 'aprovado']
    list_filter = ['aprovado']
    search_fields = ['id', 'usuario', 'nome_de_guerra']
    search_help_text = 'Você pode pesquisar por ID, usuário e nome de guerra'



@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'jornalista', 'descricao']
    search_fields = ['id', 'jornalista']
    search_help_text = 'Você pode pesquisar por ID e jornalista'


