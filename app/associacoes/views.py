from django.shortcuts import render, redirect
from django.urls import reverse
from .forms.associacoes import AssociacaoForm
from django.views.generic import View


class CadastroAssociacoesView(View):
    def get(self, request):
        associacao_form = AssociacaoForm()
        return render(
            request,
            'associacoes/pages/cadastro.html',
            context={
                'associacao_form': associacao_form
            }
        )
    
    def post(self, request):
        associacao_form = AssociacaoForm(
            request.POST
        )
        if associacao_form.is_valid():
            associacao_form.save()
            return redirect(
                reverse('jornalistas:home')
            )

        return redirect(
            reverse('associacoes:cadastro')
        )