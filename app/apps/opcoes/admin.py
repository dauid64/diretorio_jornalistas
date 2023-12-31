from django.contrib import admin
from .models import EstadoCivil, Genero, Pais, Cidades, Estados, RedesSociais, TipoDeRedeSocial, TipoDePublicacao


@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    pass


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    pass


@admin.register(Cidades)
class CidadesAdmin(admin.ModelAdmin):
    pass


@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    pass


@admin.register(RedesSociais)
class RedesSociaisAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoDeRedeSocial)
class TipoDeRedeSocialAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoDePublicacao)
class TipoDePublicacaoAdmin(admin.ModelAdmin):
    pass