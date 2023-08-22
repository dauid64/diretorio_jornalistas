from django.contrib import admin
from .models import Associacao


@admin.register(Associacao)
class AssociacaoAdmin(admin.ModelAdmin):
    pass
