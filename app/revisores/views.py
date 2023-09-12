from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from jornalistas.models import Jornalista
from revisores.models import Revisor


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


class RevisorAprovarView(View):
    def post(self, request, id):
        jornalista = Jornalista.objects.get(id=id)
        revisor_responsavel = Revisor.objects.get(usuario=request.user)
        jornalista.aprovado = True
        jornalista.revisor_responsavel = revisor_responsavel
        jornalista.save()
        return redirect(
            reverse('revisores:analise')
        )



