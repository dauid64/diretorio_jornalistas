from django.contrib import admin
from .models import Revisor


@admin.register(Revisor)
class RevisorAdmin(admin.ModelAdmin):
    list_select_related = ['usuario']
    list_display = ['id', 'usuario', 'criado_em',
                    'atualizado_em', 'get_jornalista_aprovado']
    list_filter = ['criado_em']
    search_fields = ['id', 'usuario']
    search_help_text = 'Você pode pesquisar por ID e usuário'

    def get_jornalista_aprovado(self, obj):
        return obj.usuario.jornalista.aprovado
    get_jornalista_aprovado.short_description = 'jornalista aprovado'