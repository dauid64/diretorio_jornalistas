from typing import Any
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from utils.decorators import revisor_required
from django.views.generic import View, ListView
from jornalistas.models import Jornalista
from opcoes.models import RedesSociais
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
    user_passes_test(revisor_required, login_url='jornalistas:home', redirect_field_name='next'),
    name='dispatch'
)
class RevisorAnaliseView(ListView):
    model = Jornalista
    queryset = Jornalista.objects.filter(revisor_responsavel=None).select_related('usuario').order_by('-id')
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


@method_decorator(login_required, name='dispatch')
class RevisorAprovarView(View):
    def post(self, *args, **kwargs):
        msg = ''
        status = 200
        id = kwargs['id']
        try:
            jornalista = Jornalista.objects.get(id=id)
            revisor_responsavel = Revisor.objects.get(usuario=self.request.user)
        except Jornalista.DoesNotExist:
            msg = 'Você não é um jornalista cadastrado.'
            status = 404
        except Revisor.DoesNotExist:
            msg = 'Você não tem autorização para realizar essa ação.'
            status = 404
        else:
            jornalista.aprovado = True
            jornalista.revisor_responsavel = revisor_responsavel
            jornalista.save()
            msg = 'Jornalista aprovado com sucesso!'
        return JsonResponse(
            data={
                'id': id,
                'message': msg,
                'status': status
            }
        )


@method_decorator(login_required, name='dispatch')
class RevisorReprovarView(View):
    def post(self, *args, **kwargs):
        msg = ''
        status = 200
        id = kwargs['id']

        try:
            jornalista = Jornalista.objects.get(id=id)
            revisor_responsavel = Revisor.objects.get(usuario=self.request.user)
        except Jornalista.DoesNotExist:
            msg = 'Você não é um jornalista cadastrado.'
            status = 404
        except Revisor.DoesNotExist:
            msg = 'Você não tem autorização para realizar essa ação.'
            status = 404
        else:
            jornalista.aprovado = False
            jornalista.revisor_responsavel = revisor_responsavel
            jornalista.save()
            msg = 'Jornalista reprovado com sucesso!'
        return JsonResponse(
            data={
                'id': id,
                'message': msg,
                'status': status
            }
        )


@method_decorator(login_required, name='dispatch')
@method_decorator(
    user_passes_test(revisor_required, login_url='jornalistas:home', redirect_field_name='next'),
    name='dispatch'
)
class RevisorAnalisePerfilView(View):
    def get(self, request, id):
        jornalista = get_object_or_404(
            Jornalista.objects.select_related(
                'associacao',
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
