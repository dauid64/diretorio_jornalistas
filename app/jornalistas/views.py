from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import HistoricoProfissional, Jornalista
from .forms import HistoricoForm, JornalistaForm

from obras.models import Livro, Publicao
from obras.forms import LivroForm, PublicacaoForm
from django.forms import modelformset_factory


class HomeView(View):
    def get(self, request):
        GET = request.GET
        inicial = GET.get('inicial')

        name = GET.get('name')
        jornalistas = None
        if inicial:
            jornalistas = Jornalista.objects.filter(
                nome_de_guerra__istartswith=inicial,
                # aprovado=True
            )
        if name:
            jornalistas = Jornalista.objects.filter(
                nome_de_guerra__icontains=name,
                # aprovado=True
            )
        return render(
            request,
            'jornalistas/pages/home.html',
            context={
                'jornalistas': jornalistas
            }
        )


class CadastroJornalistaView(View):
    def get(self, request):
        jornalista_form = JornalistaForm()
        historico_formset = modelformset_factory(
            HistoricoProfissional,
            form=HistoricoForm
        )
        historico_forms = historico_formset(
            prefix='historico',
            queryset=HistoricoProfissional.objects.none()
        )
        livro_formset = modelformset_factory(
            Livro,
            form=LivroForm
        )
        livro_forms = livro_formset(
            prefix='livro',
            queryset=Livro.objects.none()
        )
        publicacao_formset = modelformset_factory(
            Publicao,
            form=PublicacaoForm,
        )
        publicacao_forms = publicacao_formset(
            prefix='publicacao',
            queryset=Publicao.objects.none()
        )

        return render(
            request,
            'jornalistas/pages/cadastro.html',
            context={
                'jornalista_form': jornalista_form,
                'historico_forms': historico_forms,
                'livro_forms': livro_forms,
                'publicacao_forms': publicacao_forms
            }
        )

    def post(self, request):
        POST = request.POST
        if Jornalista.objects.filter(usuario=request.user).exists():
            return redirect(
                'jornalistas:home'
            )
        jornalista_form = JornalistaForm(POST, request.FILES)
        historico_formset = modelformset_factory(
            HistoricoProfissional,
            form=HistoricoForm
        )
        historico_forms = historico_formset(
            POST,
            prefix='historico',
        )
        livro_formset = modelformset_factory(
            Livro,
            form=LivroForm
        )
        livro_forms = livro_formset(
            POST,
            prefix='livro'
        )
        publicacao_formset = modelformset_factory(
            Publicao,
            form=PublicacaoForm
        )
        publicacao_forms = publicacao_formset(
            POST,
            prefix='publicacao'
        )
        if jornalista_form.is_valid() and historico_forms.is_valid():
            if publicacao_forms.is_valid() and livro_forms.is_valid():
                jornalista = jornalista_form.save(commit=False)
                jornalista.usuario = request.user
                jornalista.save()
                livro_forms.save(commit=False)
                livros = livro_forms.save()
                for l in livros:
                    jornalista.obras_jornalisticas.add(l.obra_jornalistica)
                historicos = historico_forms.save()
                for h in historicos:
                    jornalista.historico_profissional.add(h)
                publicacao_forms.save(commit=False)
                publicacoes = publicacao_forms.save()
                for p in publicacoes:
                    jornalista.obras_jornalisticas.add(p.obra_jornalistica)
                return redirect(
                    reverse("jornalistas:home")
                )

        return redirect(
            reverse("jornalistas:cadastrar")
        )

