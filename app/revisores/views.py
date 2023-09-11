from django.shortcuts import render
from django.views import View
from jornalistas.models import Jornalista


class RevisorAnaliseView(View):
    def get(self, request):
        jornalistas_em_analise = Jornalista.objects.filter(revisor_responsavel=None)
        return render(
            request,
            'revisores/pages/analise.html',
            context={
                'jornalistas': jornalistas_em_analise
            }
        )