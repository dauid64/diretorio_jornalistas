from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Prefetch
from django.views.generic import View
from .models import HistoricoProfissional, Jornalista
from .forms import HistoricoForm, JornalistaForm
from opcoes.forms import RedesSociaisForm
from opcoes.models import RedesSociais
from django.contrib import messages
from django.core.paginator import Paginator
from obras.models import Livro, Publicao
from revisores.models import Revisor
from obras.forms import LivroForm, PublicacaoForm


class HomeView(View):
    def get(self, request):
        GET = request.GET
        inicial = GET.get('inicial')
        nome = GET.get('nome')
        additional_url_query = ''
        jornalistas = Jornalista.objects.none()
        if inicial:
            jornalistas_aprovados = Jornalista.objects.aprovados().select_related('associacao', 'estado', 'cidade').prefetch_related(
                Prefetch(
                    'historico_profissional',
                    HistoricoProfissional.objects.filter(data_de_termino=None)
                )
            )
            jornalistas = jornalistas_aprovados.filter(
                nome_de_guerra__istartswith=inicial
            )
            additional_url_query = f'&inicial={inicial}'
        if nome:
            jornalistas_aprovados = Jornalista.objects.aprovados().select_related('associacao', 'estado', 'cidade').prefetch_related(
                Prefetch(
                    'historico_profissional',
                    HistoricoProfissional.objects.filter(data_de_termino=None)
                )
            )
            jornalistas = jornalistas_aprovados.filter(
                nome_de_guerra__icontains=nome
            )
            additional_url_query = f'&nome={nome}'
        page_obj = Paginator(jornalistas, 5)
        page_num = request.GET.get('page', 1)
        jornalistas = page_obj.get_page(page_num)
        return render(
            request,
            'jornalistas/pages/home.html',
            context={
                'jornalistas': jornalistas,
                'additional_url_query': additional_url_query
            }
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
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


class PerfilUserView(View):
    def get(self, request, id):
        jornalista = get_object_or_404(
            Jornalista.objects.select_related(
                'associacao',
                'estado',
                'cidade'
            ).prefetch_related(
                'historico_profissional',
                'obras_jornalisticas'
            ),
            id=id
        )
        redes_sociais = RedesSociais.objects.filter(jornalista=jornalista).select_related('tipo_de_rede_social')

        return render(
            request,
            'jornalistas/pages/perfil.html',
            context={
                'jornalista': jornalista,
                'redes_sociais': redes_sociais
            }
        )