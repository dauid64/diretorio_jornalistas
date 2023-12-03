from apps.jornalistas.models import Jornalista
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
import os

PER_PAGE = int(os.getenv('PER_PAGE', 5))


class HomeView(ListView):
    model = Jornalista
    queryset = Jornalista.objects.none()
    context_object_name = 'jornalistas'
    template_name = 'core/pages/home.html'

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


class ContatoView(TemplateView):
    template_name = 'core/pages/contato.html'


class SobreView(TemplateView):
    template_name = 'core/pages/sobre.html'