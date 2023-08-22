from django.contrib import admin
from .models import Jornalista, HistoricoProfissional


@admin.register(Jornalista)
class JornalistaAdmin(admin.ModelAdmin):
    pass


@admin.register(HistoricoProfissional)
class HistoricoProfissionalAdmin(admin.ModelAdmin):
    pass
