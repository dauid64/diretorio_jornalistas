from django.contrib import admin
from .models import Livro, ObraJornalistica, Publicao


@admin.register(ObraJornalistica)
class ObraJornalisticaAdmin(admin.ModelAdmin):
    pass


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass


@admin.register(Publicao)
class PublicaoAdmin(admin.ModelAdmin):
    pass