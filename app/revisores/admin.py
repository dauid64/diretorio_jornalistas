from django.contrib import admin
from .models import Revisor


@admin.register(Revisor)
class RevisorAdmin(admin.ModelAdmin):
    pass
