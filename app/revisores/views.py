from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from jornalistas.models import Jornalista
from opcoes.models import RedesSociais
from django.core.paginator import Paginator
from revisores.models import Revisor


class RevisorAnaliseView(View):
    def get(self, request):
        additional_url_query = ''
        jornalistas_em_analise = Jornalista.objects.filter(revisor_responsavel=None)
        paginator = Paginator(jornalistas_em_analise, 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        return render(
            request,
            'revisores/pages/analise.html',
            context={
                'page_obj': page_obj,
                'additional_url_query': additional_url_query
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


class RevisorReprovarView(View):
    def post(self, request, id):
        jornalista = Jornalista.objects.get(id=id)
        revisor_responsavel = Revisor.objects.get(usuario=request.user)
        jornalista.aprovado = False
        jornalista.revisor_responsavel = revisor_responsavel
        jornalista.save()
        return redirect(
            reverse('revisores:analise')
        )


class RevisorAnalisePerfilView(View):
    def get(self, request, id):
        jornalista = get_object_or_404(
            Jornalista.objects.select_related(
                'associacao',
                'estado',
                'cidade'
            ),
            id=id
        )
        redes_sociais = RedesSociais.objects.filter(jornalista=jornalista).select_related('tipo_de_rede_social')
        return render(
            request,
            'revisores/pages/analise_perfil.html',
            context={
                'jornalista': jornalista,
                'redes_sociais': redes_sociais
            }
        )