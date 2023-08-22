from django.shortcuts import render
from django.views.generic import View


class LoginUserView(View):
    def get(self, request):
        return render(
            request,
            'autenticacao/pages/login.html',
            context={}
        )