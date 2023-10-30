from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.decorators import revisor_required
from django.views.generic import View, ListView, DetailView
from jornalistas.models import Jornalista, HistoricoProfissional
from opcoes.models import RedesSociais
from django.db.models import Prefetch
from django.core.paginator import Paginator
from revisores.models import Revisor
from django.http import JsonResponse
import os

PER_PAGE = int(os.getenv('PER_PAGE', 5))


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name='dispatch'
)
@method_decorator(
    user_passes_test(revisor_required, login_url='core:home',
                     redirect_field_name='next'),
    name='dispatch'
)
class RevisorAnaliseView(ListView):
    model = Jornalista
    queryset = Jornalista.objects.filter(
        revisor_responsavel=None).select_related(
        'usuario').prefetch_related('associacoes').order_by('-id')
    template_name = 'revisores/pages/analise.html'
    context_object_name = 'jornalistas'

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        paginator = Paginator(ctx.get('jornalistas'), PER_PAGE)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        pagination_range = paginator.get_elided_page_range(page_number)
        ctx.update({
            'jornalistas': page_obj,
            'paginator': paginator,
            'pagination_range': pagination_range
        })
        return ctx


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name='dispatch'
)
@method_decorator(
    user_passes_test(revisor_required, login_url='core:home',
                     redirect_field_name='next'),
    name='dispatch'
)
class RevisorAprovarView(View):
    def post(self, *args, **kwargs):
        id = kwargs['id']
        jornalista = Jornalista.objects.get(id=id)
        revisor_responsavel = Revisor.objects.get(usuario=self.request.user)
        jornalista.aprovado = True
        jornalista.revisor_responsavel = revisor_responsavel
        jornalista.save()
        msg = 'Jornalista aprovado com sucesso!'

        return JsonResponse(
            data={
                'id': id,
                'message': msg
            }
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name='dispatch'
)
@method_decorator(
    user_passes_test(revisor_required, login_url='core:home',
                     redirect_field_name='next'),
    name='dispatch'
)
class RevisorReprovarView(View):
    def post(self, *args, **kwargs):
        id = kwargs['id']
        jornalista = Jornalista.objects.get(id=id)
        revisor_responsavel = Revisor.objects.get(usuario=self.request.user)
        jornalista.aprovado = False
        jornalista.revisor_responsavel = revisor_responsavel
        jornalista.save()
        msg = 'Jornalista reprovado com sucesso!'

        return JsonResponse(
            data={
                'id': id,
                'message': msg
            }
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name='dispatch'
)
@method_decorator(
    user_passes_test(revisor_required, login_url='core:home',
                     redirect_field_name='next'),
    name='dispatch'
)
class RevisorAnalisePerfilView(DetailView):
    model = Jornalista
    context_object_name = 'jornalista'
    template_name = 'revisores/pages/analise_perfil.html'

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related(
            Prefetch(
                'redessociais_set',
                queryset=RedesSociais.objects.all().select_related(
                    'tipo_de_rede_social'
                )
            ),
            Prefetch(
                'historicoprofissional_set',
                HistoricoProfissional.objects.all().select_related(
                    'veiculo_de_comunicacao'
                )
            )
        )
        return qs
