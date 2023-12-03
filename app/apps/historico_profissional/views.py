from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import inlineformset_factory
from django.contrib import messages
from .models import HistoricoProfissional, Referencia
from .forms import ReferenciaForm, HistoricoForm
from django.views.generic import View


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
)
class CadastroHistoricoView(View):
    def post(self, request):
        POST = request.POST
        jornalista = request.user.jornalista
        request.session['experiencia_data'] = POST
        historico_form = HistoricoForm(POST)
        referencia_formset = inlineformset_factory(
            HistoricoProfissional,
            Referencia,
            ReferenciaForm
        )
        referencia_form = referencia_formset(
            POST
        )
        if historico_form.is_valid() and referencia_form.is_valid():
            historico = historico_form.save(commit=False)
            historico.jornalista = jornalista
            historico.save()
            referencia_form.instance = historico
            referencia_form.save()
            del (request.session['experiencia_data'])
            messages.success(request, 'Experiência adicionada com sucesso!')
            return redirect(
                reverse('jornalistas:editar', kwargs={'pk': jornalista.id})
            )
        messages.warning(
            request,
            'Não foi possível adicionar experiência. Verifique os erros que ocorreram'
        )


class EditarHistoricoView(View):
    def get(self, request, pk):
        jornalista = request.user.jornalista
        historico = get_object_or_404(
            HistoricoProfissional,
            pk=pk
        )
        if historico.jornalista = jornalista:
            return redirect(
                
            )
        
