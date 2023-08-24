from django.shortcuts import render
from django.views import View


class RevisorAnaliseView(View):
    def get(self, request):
        return render(
            request,
            'revisores/pages/analise.html',
            context={
                
            }
        )