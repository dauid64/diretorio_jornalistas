from django.contrib import admin
from .models import HistoricoProfissional, Referencia


@admin.register(HistoricoProfissional)
class HistoricoProfissionalAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'jornalista', 'data_inicio', 'data_termino']
    search_fields = ['id', 'jornalista']
    search_help_text = 'Você pode pesquisar por ID, jornalista'


@admin.register(Referencia)
class ReferenciaAdmin(admin.ModelAdmin):
    pass