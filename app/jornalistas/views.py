from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import HistoricoProfissional, Jornalista
from .forms import HistoricoForm, JornalistaForm
from opcoes.forms import RedesSociaisForm
from opcoes.models import RedesSociais
from django.contrib import messages
from obras.models import Livro, Publicao, ObraJornalistica
from revisores.models import Revisor
from obras.forms import LivroForm, PublicacaoForm
from django.forms import modelformset_factory


class HomeView(View):
    def get(self, request):
        GET = request.GET
        inicial = GET.get('inicial')

        name = GET.get('name')
        jornalistas = None
        if inicial:
            jornalistas_aprovados = Jornalista.objects.aprovados()
            jornalistas = jornalistas_aprovados.filter(
                nome_de_guerra__istartswith=inicial,
                # aprovado=True
            )
        if name:
            jornalistas_aprovados = Jornalista.objects.aprovados()
            jornalistas = jornalistas_aprovados.filter(
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
        jornalist_form_data = request.session.get('register_jornalist_data', None)
        jornalista_form = JornalistaForm(jornalist_form_data)
        historico_formset = modelformset_factory(
            HistoricoProfissional,
            form=HistoricoForm
        )
        historico_forms = historico_formset(
            jornalist_form_data,
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
        redes_sociais_form = RedesSociaisForm(
            jornalist_form_data
        )

        return render(
            request,
            'jornalistas/pages/cadastro.html',
            context={
                'jornalista_form': jornalista_form,
                'historico_forms': historico_forms,
                'livro_forms': livro_forms,
                'publicacao_forms': publicacao_forms,
                'redes_sociais_form': redes_sociais_form
            }
        )

    def post(self, request):
        POST = request.POST
        request.session['register_jornalist_data'] = POST
        if Jornalista.objects.filter(usuario=request.user).exists():
            messages.warning(request, 'Você já está cadastrado')
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
        redes_sociais_form = RedesSociaisForm(
            POST
        )
        if jornalista_form.is_valid() and historico_forms.is_valid() and redes_sociais_form.is_valid():
                jornalista=jornalista_form.save(commit=False)
                jornalista.usuario = request.user
                jornalista.save()
                # livro_forms.save(commit=False)
                # livros = livro_forms.save()
                redes_sociais_list = []
                for field, key in redes_sociais_form.cleaned_data.items():
                    if key is not None:
                        match field:
                            case 'link_telegram':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=1
                                    )
                                )
                            case 'link_facebook':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=2
                                    )
                                )
                            case 'link_podcast':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=3
                                    )
                                )
                            case 'link_linkedin':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=4
                                    )
                                )
                            case 'link_twitter':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=5
                                    )
                                )
                            case 'link_site':
                                redes_sociais_list.append(
                                    RedesSociais(
                                        jornalista=jornalista,
                                        link=key,
                                        tipo_de_rede_social_id=6
                                    )
                                )
                RedesSociais.objects.bulk_create(redes_sociais_list)
                historicos = historico_forms.save()
                jornalista.historico_profissional.add(*historicos)
                # obras_jornalisticas_livros_list = []
                # for l in livros:
                #     obras_jornalisticas_livros_list.append(
                #         ObraJornalistica(
                #             l.cleaned_data['titulo'],
                #             l.cleaned_data['descricao']
                #         )
                #     )
                # jornalista.obras_jornalisticas.add(*obras_jornalisticas_livros_list)
                # jornalista.historico_profissional.add(*historicos)
                # publicacao_forms.save(commit=False)
                # publicacoes = publicacao_forms.save()
                # obras_jornalisticas_publicacoes_list = []
                # for p in publicacoes:
                #     obras_jornalisticas_publicacoes_list.append(
                #         ObraJornalistica(
                #             p.cleaned_data['titulo'],
                #             p.cleaned_data['descricao']
                #         )
                #     )
                # jornalista.obras_jornalisticas.add(*obras_jornalisticas_publicacoes_list)
                is_revisor = POST.get('is_revisor')
                print(is_revisor)
                if is_revisor == 'Sim':
                    Revisor.objects.create(
                        usuario=request.user,
                        associacao=jornalista_form.cleaned_data['associacao']
                    )
                del (request.session['register_jornalist_data'])
                return redirect(
                    reverse("jornalistas:home")
                )
        return redirect(
            reverse("jornalistas:cadastrar")
        )

