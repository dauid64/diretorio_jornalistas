from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import HistoricoProfissional, Jornalista
from .forms import HistoricoForm, JornalistaForm
from opcoes.forms import RedesSociaisForm
from opcoes.models import RedesSociais
from django.contrib import messages
from django.core.paginator import Paginator
from revisores.models import Revisor


class HomeView(View):
    def get(self, request):
        GET = request.GET
        inicial = GET.get('inicial')
        nome = GET.get('nome')
        additional_url_query = ''
        jornalistas = Jornalista.objects.none()
        if inicial:
            jornalistas_aprovados = Jornalista.objects.aprovados().select_related('associacao', 'estado', 'cidade')
            jornalistas = jornalistas_aprovados.filter(
                nome_de_guerra__istartswith=inicial
            )
            additional_url_query = f'&inicial={inicial}'
        if nome:
            jornalistas_aprovados = Jornalista.objects.aprovados().select_related('associacao', 'estado', 'cidade')
            jornalistas = jornalistas_aprovados.filter(
                nome_de_guerra__icontains=nome
            )
            additional_url_query = f'&nome={nome}'
        paginator = Paginator(jornalistas, 5)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        return render(
            request,
            'jornalistas/pages/home.html',
            context={
                'page_obj': page_obj,
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
        historico_formset = inlineformset_factory(
            Jornalista,
            HistoricoProfissional,
            form=HistoricoForm,
            extra=1
        )
        historico_forms = historico_formset(
            jornalist_form_data,
            prefix='historico',
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
        historico_formset = inlineformset_factory(
            Jornalista,
            HistoricoProfissional,
            form=HistoricoForm
        )
        historico_forms = historico_formset(
            POST,
            prefix='historico',
        )
        redes_sociais_form = RedesSociaisForm(
            POST
        )
        if jornalista_form.is_valid() and historico_forms.is_valid() and redes_sociais_form.is_valid():
            jornalista = jornalista_form.save(commit=False)
            jornalista.usuario = request.user
            jornalista.save()
            historico_forms.instance = jornalista
            historico_forms.save()
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
            ),
            id=id
        )
        redes_sociais = RedesSociais.objects.filter(jornalista=jornalista).select_related('tipo_de_rede_social')
        if request.user != jornalista.usuario:
            return render(
                request,
                'jornalistas/pages/perfil.html',
                context={
                    'jornalista': jornalista,
                    'redes_sociais': redes_sociais
                }
            )
        