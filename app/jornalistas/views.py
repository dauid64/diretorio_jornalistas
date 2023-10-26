from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Prefetch
from django.views.generic import View, ListView, DetailView
from .models import HistoricoProfissional, Jornalista
from .forms import HistoricoForm, JornalistaForm
from opcoes.forms import RedesSociaisForm
from opcoes.models import RedesSociais
from django.contrib import messages
from django.core.paginator import Paginator
from revisores.models import Revisor
import os


PER_PAGE = int(os.getenv('PER_PAGE', 5))


class HomeView(ListView):
    model = Jornalista
    queryset = Jornalista.objects.none()
    context_object_name = 'jornalistas'
    template_name = 'jornalistas/pages/home.html'

    def get_queryset(self):
        qs = super().get_queryset()
        GET = self.request.GET
        inicial = GET.get('inicial')
        nome = GET.get('nome', None)

        if inicial:
            qs = Jornalista.objects.aprovados().filter(
                    nome_de_guerra__istartswith=inicial
                ).order_by('-id')
        if nome:
            qs = Jornalista.objects.aprovados().select_related(
                'associacao').filter(
                    nome_de_guerra__icontains=nome
                ).order_by('-id')

        return qs

    def get_context_data(self):
        additional_url_query = ''
        GET = self.request.GET
        inicial = GET.get('inicial', None)
        nome = GET.get('nome', None)
        if inicial:
            additional_url_query = f'&inicial={inicial}'
        if nome:
            additional_url_query = f'&nome={inicial}'
        ctx = super().get_context_data()
        paginator = Paginator(ctx.get('jornalistas'), PER_PAGE)
        page_number = GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        pagination_range = paginator.get_elided_page_range(page_number)
        ctx.update({
            'jornalistas': page_obj,
            'paginator': paginator,
            'pagination_range': pagination_range,
            'additional_url_query': additional_url_query
        })
        return ctx


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
            jornalista_form.save_m2m()
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
            if is_revisor == 'on':
                revisor = Revisor.objects.create(
                    usuario=request.user
                )
                revisor.associacoes.add(*jornalista_form.cleaned_data['associacoes'])
            del (request.session['register_jornalist_data'])
            return redirect(
                reverse("jornalistas:home")
            )
        return redirect(
            reverse("jornalistas:cadastrar")
        )


class PerfilJornalistaView(DetailView):
    model = Jornalista
    template_name = 'jornalistas/pages/perfil.html'
    context_object_name = 'jornalista'
