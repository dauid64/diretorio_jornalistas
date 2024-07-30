from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.views.generic import View, ListView, DetailView
from .models import Jornalista, Diploma
from .forms import JornalistaForm, DiplomaForm
from apps.historico_profissional.models import HistoricoProfissional, Referencia
from apps.historico_profissional.forms import ReferenciaForm, HistoricoForm
from apps.opcoes.forms import RedesSociaisForm
from apps.opcoes.models import RedesSociais
from django.contrib import messages
from apps.autenticacao.forms import RegisterUserForm
from django.core.paginator import Paginator
from apps.revisores.models import Revisor
from django.http import HttpResponse
import os

from apps.opcoes.models import Cidades, Estados


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
            qs = Jornalista.objects.aprovados().filter(
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


class PerfilJornalistaView(DetailView):
    model = Jornalista
    template_name = 'jornalistas/pages/perfil.html'
    context_object_name = 'jornalista'


class CadastroJornalistaView(View):
    def get(self, request):
        jornalista = None
        jornalista_form = JornalistaForm()
        usuario_form = RegisterUserForm()

        # sort the cities in alphabetical order to show the user
        jornalista_form.fields["cidade"].queryset=Cidades.objects.order_by("descricao")

        diploma_formset = inlineformset_factory(
            Jornalista,
            Diploma,
            form=DiplomaForm,
            extra=1
        )

        diploma_forms = diploma_formset(
            prefix='diploma'
        )

        redes_sociais_formset = inlineformset_factory(
            Jornalista,
            RedesSociais,
            form=RedesSociaisForm,
            extra=1
        )

        redes_sociais_form = redes_sociais_formset(
            prefix='redes_sociais'
        )
        
        return render(
            request,
            'jornalistas/pages/cadastro.html',
            context={
                'jornalista': jornalista,
                'usuario_form': usuario_form,
                'jornalista_form': jornalista_form,
                'diploma_forms': diploma_forms,
                'redes_sociais_form': redes_sociais_form
            }
        )

    def post(self, request):
        POST = request.POST
        print(POST)
        FILES = request.FILES
        jornalista_form = JornalistaForm(POST, request.FILES)
        usuario_form = RegisterUserForm(POST)
        diploma_formset = inlineformset_factory(
            Jornalista,
            Diploma,
            form=DiplomaForm,
        )
        diploma_forms = diploma_formset(
            data=POST,
            files=FILES,
            prefix='diploma'
        )
        redes_sociais_formset = inlineformset_factory(
            Jornalista,
            RedesSociais,
            form=RedesSociaisForm
        )
        redes_sociais_form = redes_sociais_formset(
            POST,
            prefix='redes_sociais'
        )
        if jornalista_form.is_valid() and redes_sociais_form.is_valid()\
                and diploma_forms.is_valid() and usuario_form.is_valid():
            user = usuario_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            jornalista = jornalista_form.save(commit=False)
            jornalista.usuario = user
            jornalista.save()
            jornalista_form.save_m2m()
            diploma_forms.instance = jornalista
            diploma_forms.save()
            redes_sociais_form.instance = jornalista
            redes_sociais_form.save()
            is_revisor = POST.get('is_revisor')
            if is_revisor == 'on':
                revisor = Revisor.objects.create(
                    usuario=user
                )
                revisor.associacoes.add(
                    *jornalista_form.cleaned_data['associacoes'])
            login(request, user)
            messages.success(
                request,
                'Seu cadastro foi encaminhado para análise. Por favor, aguarde a aprovação por parte de um revisor.'
                )
            return redirect(
                reverse("core:home")
            )
        messages.warning(request,
                         'Não foi possível realizar o cadastro. Por favor, verifique os dados cadastrados.')
        return render(
            request,
            'jornalistas/pages/cadastro.html',
            context={
                'usuario_form': usuario_form,
                'jornalista_form': jornalista_form,
                'diploma_forms': diploma_forms,
                'redes_sociais_form': redes_sociais_form
            }
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
)
class EditarJornalistaView(View):
    def get(self, request, pk):
        jornalista = get_object_or_404(Jornalista, pk=pk)
        jornalista_logado = request.user.jornalista
        if jornalista != jornalista_logado:
            messages.warning(
                request,
                'Você não tem autorização para acessar essa página.'
            )
            return redirect(
                reverse('core:home')
            )
        jornalista_data = request.session.get('jornalista_data', None)
        experiencia_data = request.session.get('experiencia_data', None)
        jornalista_form = JornalistaForm(
            instance=jornalista,
            data=jornalista_data
        )

        # sort the cities in alphabetical order to show the user
        jornalista_form.fields["cidade"].queryset=Cidades.objects.order_by("descricao")

        historico_form = HistoricoForm(experiencia_data)
        referencia_formset = inlineformset_factory(
            HistoricoProfissional,
            Referencia,
            ReferenciaForm,
            extra=1
        )
        referencia_forms = referencia_formset(experiencia_data)
        diploma_formset = inlineformset_factory(
            Jornalista,
            Diploma,
            form=DiplomaForm,
            extra=1
        )
        diploma_forms = diploma_formset(
            instance=jornalista,
            prefix='diploma',
            data=jornalista_data
        )
        redes_sociais_formset = inlineformset_factory(
            Jornalista,
            RedesSociais,
            form=RedesSociaisForm,
            extra=1
        )
        redes_sociais_form = redes_sociais_formset(
            instance=jornalista,
            prefix='redes_sociais',
            data=jornalista_data
        )
        return render(
            request,
            'jornalistas/pages/editar.html',
            context={
                'jornalista': jornalista,
                'jornalista_form': jornalista_form,
                'diploma_forms': diploma_forms,
                'historico_form': historico_form,
                'referencia_forms': referencia_forms,
                'redes_sociais_form': redes_sociais_form
            }
        )

    def post(self, request, pk):
        POST = request.POST
        print(POST)
        FILES = request.FILES
        print("FILES: ", FILES)
        request.session['jornalista_data'] = POST
        jornalista = get_object_or_404(Jornalista, pk=pk)
        jornalista_logado = request.user.jornalista
        if jornalista != jornalista_logado:
            messages.warning(
                request,
                'Você não tem autorização para acessar essa página.'
            )
            return redirect(
                reverse('core:home')
            )
        jornalista_form = JornalistaForm(instance=jornalista, data=POST, files=FILES)
        diploma_formset = inlineformset_factory(
            Jornalista,
            Diploma,
            form=DiplomaForm,
        )
        diploma_forms = diploma_formset(
            instance=jornalista,
            prefix='diploma',
            data=POST,
            files=FILES
        )
        redes_sociais_formset = inlineformset_factory(
            Jornalista,
            RedesSociais,
            form=RedesSociaisForm,
        )
        redes_sociais_form = redes_sociais_formset(
            instance=jornalista,
            prefix='redes_sociais',
            data=POST
        )
        if redes_sociais_form.is_valid() and jornalista_form.is_valid() \
                and diploma_forms.is_valid():
        
            jornalista_form.save()
            diploma_forms.save()
            redes_sociais_form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            del (request.session['jornalista_data'])
            return redirect(
                reverse('jornalistas:editar', kwargs={'pk': pk})
            )

        messages.warning(request, 'Não foi possível atualizar o perfil')
        return redirect(
            reverse('jornalistas:editar', kwargs={'pk': pk})
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
)
class DownloadDiploma(View):
    def get(self, request, pk):
        diploma = get_object_or_404(
            Diploma,
            pk=pk
        )
        file_path = diploma.arquivo.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type='image/jpeg'
            )
        response['Content-Disposition'] = 'attachment; filename=Diploma.jpeg'
        return response


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
)
class DownloadCurriculo(View):
    def get(self, request, pk):
        jornalista = get_object_or_404(
            Jornalista,
            pk=pk
        )
        file_path = jornalista.curriculo.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type='application/pdf'
            )
        response['Content-Disposition'] = 'attachment; filename=Curriculo.pdf'
        return response
