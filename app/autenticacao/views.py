from django.shortcuts import render
from django.views.generic import View
from .forms import RegisterUserForm


class LoginUserView(View):
    def get(self, request):
        
        form = RegisterUserForm()

        return render(
            request,
            'autenticacao/pages/login.html',
            context={
                'form': form
            }
        )